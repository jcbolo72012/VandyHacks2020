README:

Concisely, we are building a web app were communities can host time banks, or organizations where individuals can exchange hours of specialized labor for credits, which they can then directly redeem in hours of work/service from other members of their community.

Our solution will leverage HTML/CSS/JS and Bootstrap for the frontend, and Python with Django and MySQL for the backend
Felix, Himanshu, John, Zan

Objectives:

Database Structures

    -communities
        -members

    -members
        -skills
        -communities
        -credits
        -(name, user, pass, blahblahblah)
        -requests

    -requests
        -type of skill
        -"cost"**
        -who is asking
        -who is fulfilling
        -description of task
        -community it lives in

UI
    -Homepage (Pending Requests and Validations (different subsections))
    -Profile Page (add/drop skills, see communities, etc...)
    -Marketplace Screen


