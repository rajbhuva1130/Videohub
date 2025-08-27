# Videohub - A Video Platform for Personal Development!
### A Full Stack Application

## The Overview

This project is a Full Stack application built using PostgreSQL, Python, Flask, and React. It is a video platform that allows users to post videos and comments, follow other users, and view videos based on personal interests.

### The Brief

- Develop a Full Stack Application
- Build a database and store information using PostgreSQL
- Navigate the database using Python & Flask with SQL Alchemy
- Emphasis on RESTful design to serve data programmatically
- Serve the API though a separate Front End using React
- Deliver a complete product outfitted with CRUD functionality
- Design a visually impressive Front End, with mobile responsiveness as a key element
- Deploy the application online

### Technologies Used

- PostgreSQL
- Python & Flask
- Marshmallow & SQLalchemy 
- React & JavaScript
- Git & GitHub
- Heroku 

---

## The App

We approached the development process methodically by first understanding the core components and designing the database structure carefully, paying close attention to relationships between tables. The key steps were:

1. Develop a user story and user flow.
2. Design the database backend, including relationship diagrams.
3. Develop the core backend features.
4. Attach the backend endpoints to the front end using React.
5. Form a style guide, including a wireframe, color palette, and logo.

### Design & SQL Relationships

Most of the early development was spent on designing the application's features and how they would inform the database endpoints. The goal was to create a comprehensive relationship diagram that would lead to a smooth development process. Two key design pieces were: the ability for users to easily post videos, add comments, and reply to comments; and the ability to connect with (or follow) other users to provide a curated list of videos based on their interests.
 

### The Database

With a clear idea of the backend, development began using Python, Flask, and SQLAlchemy. We started with the models, ensuring all relevant fields were included and that join tables were used for many-to-many relationships.

### The Backend

With the models in place the next step was to design the endpoints for our API - for that we started by designing the CRUD operators in the controllers and carefully designed our sterilizers and secure route. We spent most of this time designing sterilizers to make sure that we were serving all the right information to our front end whilst preventing infinite loops. 

Here is an example in the video controller using a router and secure route decorator. Here a user can post a nested comment - the nested comment data is passed additional fields and the video that had been commented on is returned.

### The Front End & React

With the backend roughed out and major endpoints ready to be used it was time for some of the team to start developing the frontend in React. Considering how powerful SQL databases can be - it was a good idea to start developing the front end before completing the backend as to tailor exactly what we wanted to be served to the front end. Our high level development of the frontend happened early on in the project along - to get a grasp of how the features hung together. We were all in agreement that developing mobile first functionality was important in regards to the user experience and the target audience we had in mind. Here we have some early wire-framing of the site layout.

### Styling & SASS

The look and feel of the site was key to a good user experience during early development we set out to develop a style guide in the form of fonts, color schemes, site layout and logos. This included developing a visual language that would be consistent across the site - buttons, forms and video windows styled in a clean and easy to use way.