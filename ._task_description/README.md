## Cement analysis with Dash

### Description

Selling cement is a crazy thing to do. When you make cement, you want to be sure that the resulting concrete is really strong in the end. But the only true way of finding out how strong that concrete will be is making a bunch of slabs for testing, wait 28 days and put them into a press. 28 DAYS! You can't possibly wait 28 days before you sell that cement. It's way too much material and you don't know where to put it in the meantime!

So. The only way to cope here is to analyze the cement (chemically and structurally), collect data and make sense of it. A lot of research on cement and its properties has been done in the past. And you also have several chemical engineers who understand how to apply this research.

All is going well in your plant, but you recently noticed that engineers spend a lot of time creating spreadsheets and sending them back and forth via email. One of them said: "Wouldn't it be neat if we had a clear dashboard that shows chemical and structural data of the cement while it is being produced?". As you happen to be a pro in data visualization, you immediately see a design coming together and with a few hours of coding, you've got a prototype at hand.

### Tasks

- Create a dashboard app with **Dash**.
- Read data from the CSV files (one file per cement, `quantities.md` describes their contents).
- Implement a way to select a cement.
- Implement a detail view that shows one cement with a graphical representation containing all strength data (2, 7 and 28 day).
- In the same detail view, make a table with the strength and laboratory data.
- Visualize the correlation between a quantity and the compressive strength. The quantity should be selectable.

You may use publicly available python libraries of your choice.

### Evaluation Criteria

- Functionality - does the app work as expected?
- Readability - how easy/hard is it to understand your implementation?
- Package organization.
- Testing (a few tests will do, but make sure to test different aspects of the app).

### If you don't know dash yet...

...that's absolutely fine. You might have a look at the [Dash Gallery](https://dash.plot.ly/gallery) and start working off one of the examples. (Hint: A dash example is usually contained in only one file. Feel free to show your organization skills by breaking it up.)

Please state in your documentation how familiar you were with dash before starting.

### Final notes

Please organize, design, test and document your code as if it were going into production.

**Don't spend more than six working hours on this!**

If you can't complete all the tasks in the given time, don't worry, as functionality is only one of the evaluation criteria. In fact, please pay a lot of attention to the evaluation criteria. Even if you only implement half of the tasks, you can still score 100% on the other criteria. Let us know in your documentation which parts are expected to be working and which are not.

Finally, please zip your project folder and send it back to your contact at alcemy.

All the best and happy coding,

Your Team at alcemy
