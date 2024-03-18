Steps to follow:

    Pre-requisites: 
        This is an example  to use the software to install
            
        Python 3.9.9
        
        Flask 3.0.1

        Postman
        
    
Steps to setup the project:

    Create a file: main.py
    Run the application: python "main.py".
    Once the Flask application is running, interact with the CRUD API using HTTP requests. 

    The endpoints to run the application using 'JSON' :
        GET '/users': Get all users.
        GET '/users/'<id>: Get a specific usee by ID.
        POST '/users:' Create a new user.
        PUT '/users/<id>': Update an existing user by ID.
        DELETE '/users/<id>': Delete an user by ID

    Example:
            Get all users:http://127.0.0.1:5000/users

            Get the user by ID:http://127.0.0.1:5000/users/2

            Create a new user:http://127.0.0.1:5000/users

            Update the user by ID:http://127.0.0.1:5000/users/1

            Delete the user by ID:http://127.0.0.1:5000/users/1

Examples for request and response format:

    1. Get All Users
       
                Endpoint: /users
       
                Method: GET
       
                Description: Retrieves all users from the database.
                
                Response Format:
                    [
                        {
                            "age": "age 1",
                            "email": "email id 1",
                            "id": 1,
                            "name": "name of the user 1"
                            
                        },
                        {
                            "age": "age 2",
                            "email": "email id 2",
                            "id": 2,
                            "name": "name of the user 2"
                        },
                        ...
                    ]
    
                Examples:
                    [
                        {
                            "age": "22",
                            "email": "josna@gmail.com",
                            "id": 1,
                            "name": "Jyothsna"
                        },
                        {
                            "age": "23",
                            "email": "sweedala@gmail.com",
                            "id": 2,
                            "name": "sweeedal"
                        },
                        ...
                    ]
    
    3. Get User by ID
    
            Endpoint: /user/<id>
            
            Method: GET
            
            Description: Retrieves a specific user by its ID.
            
            Request Format: None
            
            Response Format:
            
                [
                    {
                    
                            "age": "age 1",
                            "email": "email id 1",
                            "id": 1,
                            "name": "name of the user 1"
                    }
                    ]
    
            Example:
            
                    [
                        {
                        "age": "22",
                        "email": "josna@gmail.com",
                        "id": 1,
                        "name": "Jyothsna"
                        }
                    ]
    
    4. Create a New user
    
            Endpoint: /users
            
            Method: POST
            
            Description: Creates a new user.
            
            Request Format:
            
                    {
                
                        "age": "age 1",
                        "email": "email id 1",
                        "id": 1,
                        "name": "name of the user 1"
                    }
    
            Example:
            
                    {
                        "age": "22",
                        "email": "shravya@gmail.com",
                        "id": 1,
                        "name": "Shravya"
                    }
    
            Response Format:
            
                    [
                        {
                    
                            "age": "age 1",
                            "email": "email id 1",
                            "id": 1,
                            "name": "name of the user 1"
                        }
                    ]
    
            Example:
            
                [    
                     {
                        "age": "22",
                        "email": "shravya@gmail.com",
                        "id": 1,
                        "name": "Shravya"
                    }
                ]
    
    5. Update a user
    
            Endpoint: /users/<id>
            
            Method: PUT
            
            Description: Updates an existing user by its ID.
            
            Request Format:
            
                            {
                        
                                "name": "name of the user 1",
                                "email": "email id 1",
                                "age": "age 1"
                            }
    
            Example:
                        {
                            "name": "Shravya",
                            "email": "shravya@gmail.com",
                            "age": "32"
                        }
    
            Response Format:
            
                            [    
                                {
                            
                                    "age": "age 1",
                                    "email": "email id 1",
                                    "id": 1,
                                    "name": "name of the user 1"
                                }
                            ]
    
            Example:
                            [
                                {
                                "age": "22",
                                "email": "shravya@gmail.com",
                                "id": 1,
                                "name": "Shravya"
                                }
                            ]
    
    6. Delete a User
    
            Endpoint: /user/<id>
            
            Method: DELETE
            
            Description: Deletes a user by its ID.
            
            Request Format: None
            
            Response Format: display message
            
            Example:
            
                    User is Deleted successfully

