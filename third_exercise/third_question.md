# Article Response

This is quite a good read generally, and personally, these are the three points I find most interesting

## Readability
I agree with a lot of rules here and recognize the importance of a codebase being highly readable. The point made here
```
 The code should be written for the least technical person in the office.
```
is highly important for a start-up. Because very often, contrary to google's style guide, in a start-up, the next person reading your code is more likely going to be someone just starting in the office, or a junior developer or someone that has absolutely no idea on what the logic does. 
Putting this in mind will help you write codes much more simple to read, and less likely to waste everyone's time while of course, performing just the way a complex code will.
Concerning the rules, most of them make sense as it is always a good idea to follow a special convention when naming variables and keeping file names unique.
Though Avoiding *args and **kwargs is not what I agree with, extra args have their use cases and could make your code more readable in some scenarios, as long as they are used for what they are meant for, *when you're not sure how many arguments might be passed to your function. 
Also Using functions instead of classes is not a good idea in some cases, concept of OOP is really important and when grasped, could make some logic easier to write, for example, inheritance is a lot cleaner compared to function decorators.

## Simplicity
This is highly important and has to be a watchword in my opinion,
" As much as you can, keep it simple "
There is no point in making the codebase overly complex and increasing the onboarding time of upcoming developers.
`Rule 12 - Write Tests` is one of my favourite in this section, and I agree with having every endpoint perform the same tests in the same order, this makes the test easy to read and could serve as an indirect doc for new developers
Though he made a point of developers with less than two years experience not writing tests, I don't think this is a good approach, because personally, if they don't start now, two years later they will find tests boring and highly unimportant, better to start getting used to it and ensuring testing is part of their coding lifestyle. 
I also find the " Don't write model tests" interesting because it is contrary to what I used to believe in. And the point laid out makes a lot of sense, and besides, you will have model factories, no point specifically writing tests for models unless for the attributes and methods.

## Predictability
Every endpoint should tell a story, and all views should have a clear format to be followed, this makes debugging less of a pain and the clarity it gives is worth it.
Though concerning input sanitization, I believe this could be done in the frontend without any implication, but well its never bad to have it done on the server-side too, and bleach is a nice package, keeping business logic out of models too is a very reasonable point, and having the services in a file makes the view less clunked up, follows the DRY principle and just makes the whole codebase more beautiful to read. At this age though, I don't think not splitting your URL is necessary, as these days we have very powerful code editors and can search whatever you want with just a click. And keeping the folders organized is a plus, and in my opinion makes codebases easier to debug, as you can pinpoint the folder it is, and won't have to surf through a whole lot of codes.

Generally, this article is a good read and I appreciate that I had the chance to go through it, I have learnt quite a lot from this. Thank you Very much for sharing.