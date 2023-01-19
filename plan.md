App
    -accessKey
    -secretKey
    -item_types
    -users
        -email
        -password
        -username
        -purchases
            -Date
                -list of purchases on that date
                    -item_name
                    -item_type
                    -item_price
                    -purchase_time

#API PLANNING
-> Signing up an user
    route: /signup
    method: POST
    request_body: 
        type: form_data
        data: name
              email
              password 
              
    response_body: "User signed up succesfully"

-> Logging in user
    route: /login
    method: POST
    request_body: 
        type: form_data
        data: email/username
              password
    response_body: user_idx
                   message

-> Add a purchase
    route: /add_purchase
    method: POST
    request_body: 
        type: form_data
        data: item_name
              item_price
              item_type
    response_body: 
              message: "Item added successfully"

-> Delete a purchase
route: /delete_purchase
    method: GET
    request_body: 
        type: form_data
        data:item_id

-> Get all purchases for today
    route: /get_purchases_today
    method: GET
    request_body:
        data: user_idx
    response_body:
        list of all purchases in the following format:
            [
                {
                    "item_name": "", "item_price":"", "item_type":"", "purchase_time":""
                }
            ]
-> Get all purchases from start date and end date
route: /get_all_purchases
    method: GET
    request_body:
        data: user_idx
              start_date
              end_date
    response_body:
            data:
               [
                {
                    "item_name": "", "item_price":"", "item_type":"", "purchase_time":""
                }
            ]
-> Get the average amount of purchase till now

-> Get the most purchased item

# Planning APIs as admin user
route: /admin_user
    method: POST
    request_body: 
        type: form_data
        data: 
              
    response_body: