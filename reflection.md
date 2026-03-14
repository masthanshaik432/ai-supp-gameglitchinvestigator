# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Initially, the game looked good from a visual perspective before running anything. However, I noticed that the hints were opposite to what the goal actually was (e.g. if the goal was 56 and I typed 50 the hint was saying GO LOWER). Also, when I clicked new game, the number of attempts would go to 8 rather than the original 7.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude on this project. 
One example that AI caught and fixed correctly was the difficulty range. Initially, the range was being set to 1-100 regardless of the difficulty. However, it is now correct. 
Sometimes, Claude was not able to look at the bigger picture even though it caught a bug (in other words it smalled a small part of a problem and thought that the bug was resolved). For example, even though Claude suggested a fix for the inverted hints, I only noticed that the bug still existed (nominally for even numbers) when I tried various odd/even numbers. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

To test if a code bug was fixed, I would run the app again and run that specific scenario. One of the manual tests I ran is verifying that the scoring was happening properly and consistently. It showed me that AI's initial fix was actually shortsighted because the app would still subtract 10 points even for a perfect attempt. I had followed up requesting AI to fix this. 
AI helped me to design several pytests, nominally the score test checks. It brought up the different scenarios where the scoring could have been done differently, whether the first attempt was perfect, or whether the guess was higher or lower than the secret, and even when even/odd numbers were used (since that was a big bug in the first place).

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The reason that the secret was changing consistently in the original app was because the existing secret was not being looked at with each Streamlit rerun. 
To a friend, I would say that Streamlit reruns work like a refreshing a browser where the page reloads from scratch.
The change I made was wrapping the secret in a guard, "if "secret" not in st.session_state: st.session_state.secret = random.randint(low, high)". This allows for a already generated secret to stay in the session state (which is preserved during these Streamlit reruns).


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I would keep is using pytests to validate the outputs of runs. I would also continue to use new sessions to fix individual bugs.
For next time, I would try to provide some context of what should be happening in an app like this to the AI so it has a better understanding of how things should work. I.e. describe that this is a number guessing game with various difficulties and constant penalties etc.
This project made me a lot more critical about AI generated code because while the UI itself looked decent, the amount of backend errors were immense and there is just a lot of edge cases that AI is not able to look at, even when I briefly ask for bug reporting. 
