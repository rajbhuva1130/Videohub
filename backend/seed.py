from app import app, db, bcrypt # Import bcrypt here
from models.user import User
from models.comments import Comment, NestedComment
from models.genre import Genre
from models.video import Video
# You can remove the unused import 'from werkzeug.security import generate_password_hash'

with app.app_context():
    db.drop_all()
    db.create_all()

    # Genres
    animation = Genre(name='Animation')  # type: ignore
    writing = Genre(name='Writing')  # type: ignore
    film_and_video = Genre(name='Film & Video')  # type: ignore
    graphic_design = Genre(name='Graphic Design')  # type: ignore
    art_illustration = Genre(name='Art & Illustration')  # type: ignore
    music = Genre(name='Music')  # type: ignore
    photography = Genre(name='Photography')  # type: ignore
    ui_ux_design = Genre(name='UI/UX Design')  # type: ignore
    web_development = Genre(name='Web Development')  # type: ignore
    cooking = Genre(name='Cooking')  # type: ignore
    lifestyle = Genre(name='Lifestyle')  # type: ignore
    productivity = Genre(name='Productivity')  # type: ignore

    db.session.add_all([animation, writing, film_and_video, productivity, graphic_design, art_illustration, music, photography, ui_ux_design, web_development, cooking, lifestyle]) 

    print('Genres Created!')


    # ---------- Users ----------
    admin = User(username='Admin', email='hello@admin.com') # type: ignore
    admin.password = 'Hello1!' # Now uses the correct setter # type: ignore
    # The password_hash attribute is now set automatically by the setter.

    user1 = User(username='User One', email='user1@example.com') # type: ignore
    user1.password = 'User1!' # Now uses the correct setter # type: ignore

    user2 = User(username='User Two', email='user2@example.com') # type: ignore
    user2.password = 'User2!' # Now uses the correct setter # type: ignore

    user3 = User(username='User Three', email='user3@example.com') # type: ignore
    user3.password = 'User3!' # Now uses the correct setter # type: ignore

    user4 = User(username='User Four', email='user4@example.com') # type: ignore
    user4.password = 'User4!' # Now uses the correct setter # type: ignore

    user5 = User(username='User Five', email='user5@example.com') # type: ignore
    user5.password = 'User5!' # Now uses the correct setter # type: ignore  

    user6 = User(username='User Six', email='user6@example.com') # type: ignore
    user6.password = 'User6!' # Now uses the correct setter # type: ignore

    user7 = User(username='User Seven', email='user7@example.com') # type: ignore
    user7.password = 'User7!' # Now uses the correct setter # type: ignore  

    # Add all users to the session first (prevents SAWarning when assigning relationships)
    db.session.add_all([admin, user1, user2, user3, user4, user5, user6, user7])
    db.session.flush()  # persist them and give them ids

    # Now assign relationships (following, genres) safely
    user1.genres = [web_development, photography, music] # type: ignore
    user2.genres = [web_development, cooking, ui_ux_design] # type: ignore
    user3.genres = [web_development, music, art_illustration] # type: ignore
    user4.genres = [art_illustration, writing, film_and_video] # type: ignore
    user4.following = [user3, user2] # type: ignore
    user5.genres = [lifestyle, animation, film_and_video] # type: ignore
    user5.following = [user2, user1] # type: ignore
    user6.genres = [lifestyle, graphic_design, art_illustration] # type: ignore
    user6.following = [user5, user4, user3] # type: ignore
    user7.genres = [cooking, lifestyle] # type: ignore
    user7.following = [user5, user1, user6] # type: ignore

    # Commit the users & relationships (you can continue adding videos/comments after or before)
    db.session.flush()
    print('Users Created!')
    
    # Videos
    video1 = Video(
        title='Javascript, React & Hooks',  # type: ignore
        description='Get to grips with this tutorial for React and Hooks.',  # type: ignore
        vid_url='https://youtu.be/mxK8b99iJTg',  # type: ignore
        user=user2,  # type: ignore
        genres=[web_development, ui_ux_design])  # type: ignore

    video2 = Video(
        title='Functional Programming & Why You Should Try It!',  # type: ignore
        description='Learn the basics to functional programming in Javascript.',  # type: ignore
        vid_url='https://youtu.be/6NPfQJJEySY',  # type: ignore
        user=user2,  # type: ignore
        genres=[web_development])  # type: ignore

    video3 = Video(
        title='Lighting is Everything',  # type: ignore
        description='Tips and tricks to properly light your environment for filming and photography.',  # type: ignore
        vid_url='https://youtu.be/flc5iP0KwTg',  # type: ignore
        user=user1,  # type: ignore
        genres=[photography, film_and_video])  # type: ignore

    video4 = Video(
        title='Choose Your Lens',  # type: ignore
        description='A deep dive into the best lens for the job.',  # type: ignore
        vid_url='https://youtu.be/BE6H5C-g6JA',  # type: ignore
        user=user1,  # type: ignore
        genres=[photography, film_and_video])  # type: ignore

    video5 = Video(
        title='Tips For Music Photography',  # type: ignore
        description='Get the best out of your concert photos with these simple tricks.',  # type: ignore
        vid_url='https://youtu.be/-D8HTk4BnQI',  # type: ignore
        user=user1,  # type: ignore
        genres=[photography])  # type: ignore

    video6 = Video(
        title='Guitar Practice that ISN\'T Stairway To Heaven',  # type: ignore
        description='Pro habits to develop while learnign guitar.',  # type: ignore
        vid_url='https://youtu.be/PfndlSCeWeo',  # type: ignore
        user=user3,  # type: ignore
        genres=[music, lifestyle])  # type: ignore

    video7 = Video(
        title='Get That Good Sound',  # type: ignore
        description='What to look for when upgrading your Amp.',  # type: ignore
        vid_url='https://youtu.be/aW0akNVYIRs',  # type: ignore
        user=user3,  # type: ignore
        genres=[music])  # type: ignore

    video8 = Video(
        title='Learn To Paint Like Bob Ross',  # type: ignore
        description='Definitive guide to painting like painting like Bob Ross.',  # type: ignore
        vid_url='https://youtu.be/mYAmSXpeFjM',  # type: ignore
        user=user5,  # type: ignore
        genres=[art_illustration])  # type: ignore

    video9 = Video(
        title='Learn to Doodle',  # type: ignore
        description='Doodling and the art of making a mess!',  # type: ignore
        vid_url='https://youtu.be/W2HDsQGHWQk',  # type: ignore
        user=user5,  # type: ignore
        genres=[art_illustration, graphic_design])  # type: ignore

    video10 = Video(
        title='Animation - Where to Start',  # type: ignore
        description='A beginners guide to animation.',  # type: ignore
        vid_url='https://youtu.be/Cw-_vMMiaRo',  # type: ignore
        user=user5,  # type: ignore
        genres=[animation, art_illustration])  # type: ignore

    video11 = Video(
        title='Photoshop Shortcuts Everyone Should Know!',  # type: ignore
        description='Speed up your workflow with theese must use shortcuts.',  # type: ignore
        vid_url='https://youtu.be/1732S1rlHOM',  # type: ignore
        user=user5,  # type: ignore
        genres=[graphic_design])  # type: ignore

    video12 = Video(
        title='Declutter.',  # type: ignore
        description='Declutter and other tips for a happy habitat.',  # type: ignore
        vid_url='https://youtu.be/cZHUmiJQKBY',  # type: ignore
        user=user6,  # type: ignore
        genres=[lifestyle])  # type: ignore

    video13 = Video(
        title='Learn How To Learn',  # type: ignore
        description='The habit of learning and the pattern of growth.',  # type: ignore
        vid_url='https://youtu.be/FplJGbt6Iys',  # type: ignore
        user=user6,  # type: ignore
        genres=[lifestyle])  # type: ignore

    video14 = Video(
        title='Ferment The Planet',  # type: ignore
        description='Where to start your fermentation journey.',  # type: ignore
        vid_url='https://youtu.be/iiNl0Jv6xTw',  # type: ignore
        user=user7,  # type: ignore
        genres=[cooking]  # type: ignore
    )

    db.session.add_all([video1, video2, video3, video4, video5, video6, video7, video8, video9, video10, video11, video12, video13, video14])

    print('Videos Created!')
    
    # Comments
    comment1_vid1 = Comment(
        content='Great tutorial!',  # type: ignore
        video=video1,  # type: ignore
        user=user3)  # type: ignore

    comment2_vid1 = Comment(
        content='This was interesting, but can you help me fix my code?',  # type: ignore
        video=video1,  # type: ignore
        user=user4)  # type: ignore

    comment1_vid2 = Comment(
        content='I hope everyone enjoyed my tutorial!',  # type: ignore
        video=video2,  # type: ignore
        user=user2)  # type: ignore

    comment1_vid3 = Comment(
        content='This will definitely help me with a future project 😁',  # type: ignore
        video=video3,  # type: ignore
        user=user5)  # type: ignore

    comment1_vid4 = Comment(
        content='Very informative, thank you!',  # type: ignore
        video=video4,  # type: ignore
        user=user6)  # type: ignore

    comment2_vid4 = Comment(
        content='⭐️⭐️⭐️',  # type: ignore
        video=video4,  # type: ignore
        user=user3)  # type: ignore

    comment3_vid4 = Comment(
        content='Top tips!',  # type: ignore
        video=video4,  # type: ignore
        user=user2)  # type: ignore

    comment1_vid5 = Comment(
        content='But I LIKE stairway to heaven...',  # type: ignore
        video=video6,  # type: ignore
        user=user2)  # type: ignore

    comment2_vid5 = Comment(
        content='This will definitely help me practice at home!',  # type: ignore
        video=video6,  # type: ignore
        user=user6)  # type: ignore

    comment1_vid6 = Comment(
        content='Great guide thanks!',  # type: ignore
        video=video7,  # type: ignore
        user=user6)  # type: ignore

    comment1_vid7 = Comment(
        content='I forgot how much i enjoy doodling!',  # type: ignore
        video=video9,  # type: ignore
        user=user2)  # type: ignore

    comment2_vid7 = Comment(
        content='Great way to keep myself pre-occupied!',  # type: ignore
        video=video9,  # type: ignore
        user=user4)  # type: ignore

    comment1_vid8 = Comment(
        content='I didn\'t even know half of these! Love it.',  # type: ignore
        video=video11,  # type: ignore
        user=user3)  # type: ignore

    comment1_vid9 = Comment(
        content='This looks very satisfying!',  # type: ignore
        video=video12,  # type: ignore
        user=user1)  # type: ignore

    comment1_vid10 = Comment(
        content='Cant wait to start my ferment collection!',  # type: ignore
        video=video14,  # type: ignore
        user=user2)  # type: ignore

    comment2_vid10 = Comment(
        content='Love the breakdown!',  # type: ignore
        video=video14,  # type: ignore
        user=user5)  # type: ignore

    db.session.add_all([comment1_vid1, comment2_vid1, comment1_vid2, comment1_vid3, comment1_vid4, comment2_vid4, comment3_vid4, comment1_vid5, comment2_vid5, comment1_vid6, comment1_vid7, comment2_vid7, comment1_vid8, comment1_vid9, comment1_vid10, comment2_vid10])

    print('Comments Created!')

    # Nested Comments
    nested_comment_1 = NestedComment(
        nested_content='No 😊',  # type: ignore
        user=user2,  # type: ignore
        comment=comment2_vid1)  # type: ignore

    nested_comment_2 = NestedComment(
        nested_content='Thank you!',  # type: ignore
        user=user2,  # type: ignore
        comment=comment1_vid1)  # type: ignore
        
    nested_comment_3 = NestedComment(
        nested_content='I can\'t wait to see what you are working on!',  # type: ignore
        user=user6,  # type: ignore
        comment=comment1_vid3)  # type: ignore

    nested_comment_4 = NestedComment(
        nested_content='Me too!',  # type: ignore
        user=user1,  # type: ignore
        comment=comment1_vid3)  # type: ignore

    nested_comment_5 = NestedComment(
        nested_content='I agree!',  # type: ignore
        user=user2,  # type: ignore
        comment=comment2_vid7)  # type: ignore

    nested_comment_6 = NestedComment(
        nested_content='Cant wait for that sweet and sour crunch!',  # type: ignore
        user=user2,  # type: ignore
        comment=comment1_vid10)  # type: ignore

    nested_comment_7 = NestedComment(
        nested_content='Sorry! Its been banned 😂',  # type: ignore
        user=user3,  # type: ignore
        comment=comment1_vid5)  # type: ignore

    nested_comment_8 = NestedComment(
        nested_content='It\'ll change your life! Promise.',  # type: ignore
        user=user6,  # type: ignore
        comment=comment1_vid9)  # type: ignore

    db.session.add_all([nested_comment_1, nested_comment_2, nested_comment_3, nested_comment_4, nested_comment_5, nested_comment_6, nested_comment_7, nested_comment_8])

    print('Nested Comments Created!')
    
    db.session.commit()

    print('Adding to database...')

    print('Everything works!')