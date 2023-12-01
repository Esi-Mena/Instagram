In order to manually test the website I went through the scenarios outlined by the user stories and our tests. While the website was generally very polished I found 6 bugs, 4 of which were minor and 2 are very complex
- - - - - - - - - - - - - - - - - - -
Minor bugs
- There is no error message when you enter the wrong username/password. It just goes back to the login page with no indication of what you did wrong.
- When you upload an image to post there's no indication that the upload worked until you post it.
- The caption repeats twice on the comment adding page. The comments themselves show as intended.
- User bios don't show up for some users, but they do for others. However, the user bio is saved regardless as when I went to edit my bio that wasn't showing the correct bio was still shown on the editing page.
- - - - - - - - - - - - - - - - - - -
Major bugs
- Both major bugs are based on the same problem- images uploaded to the site are only being saved temporarily. Once the commit is updated again, all images that have been uploaded in the current commit are not saved and thus disappear from the program.
- Images on posts uploaded by users go away after commits.
- Users profile pictures don't save after commits, and their profiles become broken after the commit because of this.
- Fixing these bugs would require the implementation of a new saved storage system to store all uploaded images.
