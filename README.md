# API for CMS Application
   - The database should contain three tables named User, Post/Blog, and Like.
   - The User table should store user information such as user ID, name, email, password, and
   - other relevant details.
   - 3. The Post/Blog table should store post/blog information such as post ID, title, description,
   - content, creation date, and other relevant details.
   - 4. The Like table should store information about the likes of each post/blog, such as like ID,post ID, user ID, and other relevant details.
   - CRUD function for every table(User,Post,like)(To perform any crud operation user needs to be authenticated and should pass its access token as authorization)
    - Create API: To add new user/post/like to the corresponding table.
    - Read API: To retrieve a specific user/post/like from the corresponding table.
    - Update API: To update the details of a specific user/post/like in the corresponding table.
    - Delete API: To delete a specific user/post/like from the corresponding table.

   - The GET all post/blog API should also return the number of likes for each post/blog.
   - Access to the PUT/DELETE APIs for the Post/Blog table should be restricted to the owner of the post/blog.
   - Any user can access the GET API for a post/blog if it is public.



# API for each task
 |Method     | URL |Description|
 | `POST`| http://127.0.0.1:8000/api/user/ | Create User |
 | `GET` | http://127.0.0.1:8000/api/user/ | List Of registered Users with details|
 | `PUT` | http://127.0.0.1:8000/api/user/18/| Update User |
 | `PATCH` | http://127.0.0.1:8000/api/user/18/ | Update Partial Details Of User whose id=18|
 | `Delete`|http://127.0.0.1:8000/api/user/18/ | Delete User whose id=18|
 | `POST`|http://127.0.0.1:8000/api/refreshtoken/| Get Access JWT Token with refresh token |
 | `POST`|http://127.0.0.1:8000/api/post/ | Create Post|
 | `GET`| http://127.0.0.1:8000/api/post/| Retrieve Posts|
 | `GET`| http://127.0.0.1:8000/api/post/11/ | Retrieve Post whose id=11|
 | `DELETE`|http://127.0.0.1:8000/api/post/15/| Delete post whose id=15|
 | `PATCH`|http://127.0.0.1:8000/api/post/11/| Update Partial Deatails Of Post whose id=11|
 | `PUT`|http://127.0.0.1:8000/api/post/11/ |Update Complete Deatils Of a Post|
 | `POST`|http://127.0.0.1:8000/api/likepost/|Like a post by passing the post_id|
 | `GET`|http://127.0.0.1:8000/api/likepost/ | Retrieve The Liked Posts|
 | `GET`|http://127.0.0.1:8000/api/likepost/10/ |Retrieve liked post having id=10|
 | `DELETE`| http://127.0.0.1:8000/api/likepost/10/ | Delete a liked data from like table id=10|


