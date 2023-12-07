Github Copilot review
- - - - - - - - - - - - - - - - - - -
My Experience
- My experience started with me being forced to enter my payment information to use the free trial. I dislike any subscription service that forces you to enter your payment information to try their free trial. It's just manipulative practice.
- I do like how I can opt out of getting suggested code snippets from others. Of course all AI stuff is taken from other people's work but I'd really rather it at least be remixed.
- I decided to test the AI by trying to use it to create an image preview for the upload photo page, which I had tried to do by myself but had failed at.
- After reading through some of the documentation, I learned that I could ask the AI to write code by writing a comment. So I wrote a comment in the upload photo HTML page asking it to write code for a confirmation message. Then when I went to the next line it gave me a suggestion for a confirmation message. 
- I then got a really weird error about databases. Last time I was running the server locally I did not get an error like this. Our hosted server is running fine. When I deleted the Copilot code the local running was still broken so it's not its fault.
- In order to test Github Copilot I decided to use the chat feature to tell it about the problem and see if it could at least guide me in the right direction. It gave me a bunch of information about databases, but I don't know anything about our database. However, the code examples it gave could be used as reference to find the database information and figure out what's broken about it.
- Thanks to the examples, I was quickly able to identify the part of our settings.py that was in charge of databases. Nothing about our database code seemed wrong to me- it worked by taking the relevant information from the hosts computer and using it in the database. The only thing that seemed potentially suspicious was the install for the database adapter, which I did not remember doing. So I followed the install instructions given by Copilot and tried to run the server again.
- The database was still not working. The error messages says I need to supply the engine value. However, the engine is definitely supplied here- it's the only thing that's not a variable. I decided to ask Github Copilot again, this time on the settings.py file so it could see it.
- The AI said our database code appears to be set up correctly, so it's likely the condition that we're using (checking if the variables for the database have been found) isn't working properly. It gave me some debug code to check if that's the issue.
- When I ran the debug code it turned out that was in fact the problem. All of the variables printed out were assigned as none and the database code was not running. It seems like these variables don't exist on my machine anymore? I'm not sure what caused this to happen but Copilot gave me instructions on how to fix the problem. 
- After almost 2 hours of arduous bug fixing and installs where literally everything that could possibly go wrong went wrong I finally fixed the problem and got another error (that error was really easy to fix I didn't even need Github Copilot). A notable moment was when Github Copilot didn't have access to what operating system I was using and gave me the wrong command as a result. Admittedly having Github Copilot there probably reduced the time to fix it by at least half if not more...
- My biggest issue with Github Copilot during this process is that it lead me to believe that I had successfully installed the database adapter at the beginning but I actually needed to perform a larger process. I could've skipped several steps if it had informed me of the bigger install at the beginning.
- Now that the website was finally FINALLY RUNNING I could now go see if the code Github Copilot gave for the photos would work. I also made sure to thank the AI for helping with my problem. 
- However I was slightly distracted by the fact that ALL THE LOCAL DATA FOR THE SITE HAD BEEN ERASED. What happened? Huh?????
- Anyway the code for the image confirmation didn't work. Eventually I got code from the AI that made the preview work but now you can't replace the image once you've uploaded it 
- After yet another big journey with Github Copilot I was able to get photo previews to work, but at the cost of being able to change your upload while on the upload_photo page. Determined not to lose this feature, I set forward yet again
- I had learned more about how Github Copilot works since my last attempt, and I now know that it only looks at the text that's on screen. In order for it to see an entire file you have to select all the code in that file. After I deleted the code I had worked on before and restored the old code, I asked Copilot again how to add the image previews.
- This time the process of adding previews went smoothly! The suggestions were much better now that Copilot was looking at the whole page, and my increased code knowledge allowed me to make more of my own edits and suggestions. It only took about 30 minutes to have both file changing and image previews working. Thank you, Github Copilot!
- - - - - - - - - - - - - - - - - - -
Review
- - - - - - - - - - - - - - - - - - -
Over the course of 4 hours, I slowly learned to appreciate Github Copilot. While the lack of instruction on how to properly feed it information was annoying, once I figured out how to do it the AI worked very well. Its direct integration with my code made it much easier to use then Chat GPT, which I have never been able to get a proper handle of. I think it works best as a replacement for a human, when a human is not avaliable. I would much prefer to have discussed this with a human, to be clear. There were many times where Copilot massively misinterpreted the basics of what I wanted and this often ended up sending me on large tangents that I would realize in hindsight were completely useless. In addition the AI often used very complex and technical language that was clearly not suited to someone asking the sort of questions I was, which made it difficult to learn anything from the experience. The only times I learned anything was when sheer exposure forced me to. If I had to boil down Github Copilot into a simple concept, I would say that it's an AI version of Stack Exchange and Google searching, which is better than both of those but still quite frustrating. In addition, since this is a tool made by coders, for coders many of my usual ethical concerns don't apply. Overall, if I need to use Github Copilot at a future workplace, I think I would be okay with it. It can be very helpful as long as you know what you're doing to some extent. 