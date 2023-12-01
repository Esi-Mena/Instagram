# PixlPix Devops
## Introduction
Pixlpix is an social media web-abb made for users to share images. It is written in python using django. The web server and hosting are both handled using the digital ocean platform. The goal for pixlpix is to add more features with new ways for the users to connect with eachother while also maintaining and improving current features. 
## Development Procedures
### Github
The development takes place on the github repo, if you are planning on developing a large feature it would be best if the repo was branched and then developed fully until implemented. When simply fixing bugs and working on small features, just working with a clone of the repo is acceptaple. Just be sure to keep the github and your local machine in sync as to avoid merge errors. 
### Coding Practice
To keep the coding practice simple, keep code as efficent as possible, and leave comments on code at the very least explaining what the section of code is doing. It is recommended that whomever is writing code should leave a good amount of comments explaining what the code is doing, and how the code itself works incase of errors with the code. 
### Testing 
Along with writing code, coders should write tests along side the code they are writing to prevent errors and bugs as much as possible. Developers should always follow test driven development. Test code should be 50% of the code total, and cover 90% of the application. These numbers are a not a requirement but should be within 5% as best practice. 
## Deployment Procedures
All code should be deployed to the github. Once a test server is up, there should never be any undeployed code unless the developer is actively writing the code. Even if the code does not work and there are errors it should be pushed when the developer is done working to avoid merge errors and to allow for other developers to see what is being done and help fix it. Digital ocean will automatically push changes into production. Once the test server is set up changes will first go to a test server to ensure that everything is working properly then pushed to the production deployment. 
## Issues
### Issue Logging 
All issues will be logged into the build-in issues tab of github. Q&A developers should work to both find this issues and flag them and help resolve them when needed. When opening an issue, the following information is to be provided: Name of Issue, location of issue in the code(if known), a very detailed description of the issue, how it was found, and the date found. When an issue is resolved the following information must be provided: Date resolved, how the issue was resolved, location of the issue in the code, and how the fix could effect other features. All issues should be resolved as quickly as possible. 
### Issue Types
Issues will be defined in the following levels. Level 3 - a very minor issue where the app still runs, but a minor feature may not work as expected. Level 2 - a minor feature does not work, or a major feature is not working properly. Level 1 - A major feature is not working and the app is not functioning. 
### Response time to Issues
Level 3 - issues should be fixed within a few days but development should still proceed as planned.

Level 2 - issues should be fixed as soon as possible but development should still proceed but be slowed in order to fix the issue. 

Level 1 - Development should halt and devlopers should only work to fix the issue until it is resolved. 
## Scaling
The project is on digital ocean which is scalable. When volume on the website increases we can increase the amount of resources needed from digital ocean. When more sever space is needed the digital ocean tier can be uprgraded, as with the speed of the server.
# Data Management
This section will be on the data management for pixlpix.
## Types of Data collected
Most of the data from users that will be saved is whatever the user posts to their profile. Things such as posts, captions, comments, and profile pictures are the data that we will save from the user as it is neccesary for the app to be funcitonal. Therefore the main data type that we will have is images, along with some text and user information (email, name, info they use when they create the account).
## Data Collection Methods
All the data we currently collect will be collected by forms. Forms are currently the only way that pixlpix gets data from its user. Pixlpix does not collect anything from the user that the user does not upload to the site. 
## User Consent
There will be a user consent form created allowing the user to agree to our data collection when they create an account on the site. Since the only data that is kept on users is to keep the core features of the site working, if the user does not accept they will not be able to create an account. 
## Data Storage
A storage space on digital ocean will be created. This storage space will contain all images uploaded to the website, such as profile pictures and posts. All other user information such as account name,email, comments, captions and such will be kept in the database.  
## Data Backups
A script will be created to automatically backup all data to a local location on set intervals. This is in the case that the storage space and database have an error, the pixlpix team can rollback to the latest backup to keep the user experience positive. 
## Data Access/Governance
PixlPix owns all of the data uploaded to the site. Pixlpix will not sell this data to anyone else and intends to only use it to better the user experience. Pixlpix and digital ocean are the only companies that will be able to see your data. The data will be public on the pixlpix website unless a post is deleted. However pixlpix will still have the image from the post, but it will no longer be publicly accessible from the internet. 
