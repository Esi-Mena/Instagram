# Milestone 1
## Maxwell Seybert - Tester
### What I did for Mileston 1
- For milestone 1 I placed my django app from BACS350 and tweaked it a little bit because it did not work with some updates that had been made. I also used this app to refamilliarize myself with django and how it works.
- Then I worked on establishing hosting. Initally we were going to use digital ocean to host our web app howver digital ocean has had many issues. When using digital ocean the deployment did not work at first (which was not a suprise to me) so I began to debug. After a few attempts to debug digital ocean gave me an infinite deployment that never finished bulding but in my logs it says there was a successful attempt and then an immediate fail despite me not attempting another deployment. 
- After meeting with both the professor and my group we made the choice that we should move to a different hosting platform. In the end we went with railway as our hosting platform. Railway is a pretty straigtforward and cheap hosting platform that will meet our needs for the project. It has was to implement a production database and automatically updates with our github repo being updated. 
### What will I do - testing milestone 2
- I think we are supposed to switch roles for each milestone but I will write this with the impression of what the tester should do next. Again I am confused with what exactly is wanted for this as the digital ocean hosting issues are affecting the class instruction website as well, and trying to access the requirements through github can be confusing. However, for the next milestone I think that the tester should plan how testing is going to work (testing our code, and our hosting) and a plan for both of those things to be acheived. 
### Concerns and Challenges
- In the "what will I do" section I touched on a lot of the major concerns and challenges. It is difficult to understand how to move forward without the class site. Although looking through the github is an okay fix for us to understand how to move forward it is not as convenient as using the class site. Challenges that I had with hosting were mostly found when using digital ocean and the issues that digital ocean is having. Once switching to railway I was met with a lot less issues, although there were a few. Firstly, railway does not automatically let you choose a folder directory when hosting at first, but this issue is easily solved when going into your settings tab. Another issue I had was creating a procfile and making sure my requirements were correct. I used pip freeze to understand the requirements however the hosting needed gunicorn installed even though I did not have that installed on my local machine. I also found that in the procfile I needed to state that migrations needed to be made. 
### Engineering Investment
- 1hr and 30mins w group
- 2 hours getting myself fammilar with django again
- 6 hours attempting to work with digital ocean
- 1 hr and 30mins getting railway hosting working
### Hosting Location
 - Link to our hosted web app - https://instagram-production.up.railway.app/
### Video Demo - 