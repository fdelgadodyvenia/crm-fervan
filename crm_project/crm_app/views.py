from django.shortcuts import render
from .forms import ClientForm
from libs.maria_db_utils import transform_db, write_to_db, read_from_db, create_connection

def insert_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            birth_date = form.cleaned_data['birth_date']
            potential_client_level = form.cleaned_data['potential_client_level']
            next_action = form.cleaned_data['next_action']
            notes = form.cleaned_data['notes']
            ######################################################
            columns = {
                "name": "VARCHAR(255) NOT NULL",
                "surname": "VARCHAR(255) NOT NULL",
                "email": "VARCHAR(255) NOT NULL",
                "birth_date": "VARCHAR(255) NOT NULL",
                "potential_client_level": "VARCHAR(255) NOT NULL",
                "next_action": "VARCHAR(255) NOT NULL",
                "notes": "VARCHAR(255) NOT NULL"
            }
            data = {
            "name": name,
            "surname": surname,
            "email": email,
            "birth_date": birth_date,
            "potential_client_level": potential_client_level,
            "next_action": next_action,
            "notes": notes
            }
            # Call your custom functions here
            manage_db(columns=columns, data=data, operation="write")
            ######################################################
            return render(request, 'crm_app/success.html')
    else:
        form = ClientForm()
    return render(request, 'crm_app/potencial_clients.html', {'form': form})

def list_clients(request):
    #############
    columns = {
        "name": "VARCHAR(255) NOT NULL",
        "surname": "VARCHAR(255) NOT NULL",
        "email": "VARCHAR(255) NOT NULL",
        "birth_date": "VARCHAR(255) NOT NULL",
        "potential_client_level": "VARCHAR(255) NOT NULL",
        "next_action": "VARCHAR(255) NOT NULL",
        "notes": "VARCHAR(255) NOT NULL"
    }          
    clients=manage_db(columns, operation="read")
    #############
    print (clients)
    return render(request, 'crm_app/list_clients.html', {'clients': clients})

def manage_db(columns:list=None, operation:str="read", data: dict = None):
    # Replace this with your actual function logic
    connection = create_connection("maria-db", "admin", "admin", "metastore_db")
    
     # Create table with dynamic columns
    columns_definitions = ', '.join([f"{col} {definition}" for col, definition in columns.items()])
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS potential_clients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        {columns_definitions}
    )
    """
    transform_db(connection, create_table_query)

    if operation == "write" and data:
        columns_names = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        insert_query = f"INSERT INTO potential_clients ({columns_names}) VALUES ({placeholders})"
        write_to_db(connection, insert_query, tuple(data.values()))
        return 0
    
    elif operation == "read":
        select_query = f"SELECT * FROM potential_clients"
        cursor = connection.cursor()
        cursor.execute(select_query)
        rows = cursor.fetchall()
        print(rows)
        return rows
