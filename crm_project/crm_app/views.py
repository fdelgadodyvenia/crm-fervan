from django.shortcuts import render
from .forms import ClientForm
from libs.maria_db_utils import transform_db, write_to_db, read_from_db, create_connection

def get_name(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            ######################################################
            # Call your custom functions here
            manage_db(name, surname, "write")
            ######################################################
            return render(request, 'crm_app/success.html', {'name': name, 'surname': surname})
    else:
        form = ClientForm()
    return render(request, 'crm_app/potencial_clients.html', {'form': form})

def list_clients(request):
    #############
    clients=manage_db(operation="read")
    #############
    return render(request, 'crm_app/list_clients.html', {'clients': clients})

def manage_db(name:str="", surname:str="", operation:str="read"):
    # Replace this with your actual function logic
    connection = create_connection("maria-db", "admin", "admin", "metastore_db")
    
    # Create table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS potencial_clients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL
    )
    """
    transform_db(connection, create_table_query)
    
    # Write to DB
    insert_query = """
    INSERT INTO potencial_clients (name, surname) VALUES (%s, %s)
    """
    
    if operation=="write":
        data_to_insert = (name, surname)
        write_to_db(connection, insert_query, data_to_insert)
        return 0
    
    elif operation=="read":
        select_query = "SELECT * FROM potencial_clients"
        rows = read_from_db(connection, select_query)
        for row in rows:
            print(row)
        return rows
