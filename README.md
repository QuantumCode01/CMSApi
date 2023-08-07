# API for CMS Application
   - The database should contain three tables named User, Post/Blog, and Like.
   - The User table should store user information such as user ID, name, email, password, and
   - other relevant details.
   - 3. The Post/Blog table should store post/blog information such as post ID, title, description,
   - content, creation date, and other relevant details.
   - 4. The Like table should store information about the likes of each post/blog, such as like ID,post ID, user ID, and other relevant details.
   - CRUD function for every table(User,Post,like)
    - Create API: To add new user/post/like to the corresponding table.
    - Read API: To retrieve a specific user/post/like from the corresponding table.
    - Update API: To update the details of a specific user/post/like in the corresponding table.
    - Delete API: To delete a specific user/post/like from the corresponding table.

   - The GET all post/blog API should also return the number of likes for each post/blog.
   - Access to the PUT/DELETE APIs for the Post/Blog table should be restricted to the owner of the post/blog.
   - Any user can access the GET API for a post/blog if it is public.

# API for every method

         | Method | URL | Description |
| :---         |     :---:      |     :---: |
| `GET`   |  http://127.0.0.1:8000/api/elevator/    | Retrieve details of all elevators created    |
| `GET`   |  http://127.0.0.1:8000/api/elevator/1   | Retrieve details of elevator whose id=1   |
| `POST`   |http://127.0.0.1:8000/api/elevator/| Create an elevator by passing elevator_id, current_floor,operational, is_busy, door| 
| `POST`   | http://127.0.0.1:8000/api/Person/ |Create the Person's record by passing requesting_floor and closest elevator is assigned to the person|
| `GET`   | http://127.0.0.1:8000/api/Person/| Retrieve details of all Persons with assigned elevator   |
| `GET`   | http://127.0.0.1:8000/api/Person/6| Retrieve details of individual Person with assigned elevator having id=6   |
| `PATCH`   |http://127.0.0.1:8000/api/Person/6     | Enter the destination_floor for the person with id=6 so that elevator moves towards the destination floor     |