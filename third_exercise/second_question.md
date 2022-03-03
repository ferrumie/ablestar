## Legacy Code

When it comes to Legacy codes there is one thing I always keep in mind,
and that is to never assume, Assuming the code isn't properly written, or a part I don't understand works. I love to have a high-level knowledge of the codebase at least. This gives me a very good idea of what it is about and makes the decision to refactor or leave alone relatively easier.

### When should Legacy code be left alone or refactored
- I believe legacy codes should have priority tags, if a legacy code contains bugs or performance issues, then there will be higher priority to refactor as soon as possible compared to a piece of code that is maybe just not looking right due to an old syntax that might be deprecated soon

- If Looking at a piece of code, I see a thing or two that can be improved, maybe during my free time and there aren't many tasks to do, I can just take it on, raise a refactor issue and try to mess around a little bit. Checkup the tests, try to run through the lines because you gain more understanding about a piece of code when you play around with it rather than just staring at it.

- If it is during a task or there is a lot of work at hand, I don't go into refactoring immediately, I try to note it down and maybe refactor piece by piece, and gradually turn it into what I want it to be over time. As long as there are no bugs or performance issues with the code

- I will check up the unit tests if there are any, check if they are up to date, write some new ones to test what the code does and not what it should do. I will also check up on the documentation about the code.

- I tend to collaborate with other developers as they might know more about the codebase than I do, and a little discussion might reveal quite a lot of info about the code.

- If there is a need to refactor the old code. I ensure I make the refactor as minimal as possible and I avoid changing what I do not need to.

- I value refactoring over rewriting, most times there is never a need to completely change the logic. But if there is a need to rewrite, rather than delete, I will prefer to mark  the old code as deprecated for a while, checking how the new code fairs just to be sure i didn't break anything