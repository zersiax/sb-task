# coding challenge notes

These are stream-of-consciousness-style notes while reading the challenge requirements and building them out. I hope these will give insight into why certain choices were made.

## Initial

- This is a Python/Django application. That means virtual environments of some kind are necessary. Docker is overkill for this, and to keep with semver and various other development best practices we'll go with pipenv.

- We are building a list of books per user. We are going to need a books table. A user has many books.
  - Title
  - Author
  - Rating
  - Poster (FK)

- We will use a customized User model. This decision was taken mainly to be more future-proof. The fictitious roadmap indicates various social features might be added in the future, it makes sense to get a tighter level of control over the User model.

- Database backend will be relational. Although it makes sense for NoSQL such as MongoDB to be used for the majority of use cases in this app, things like dashboards that run on the entire current collection of books become tedious and there are no real benefits of going with mongoDB for the rest in this case.

- CSS framework will be Bootstrap to make it look at least somewhat modern. 

- The application will be hosted up on Heroku.

- The dashboard features operate on the entire books table. At this point, who posted the book doesn't appear to matter.

- One requirement, the most read books, seems technically not feasible without a significant amount of work. This can be done various ways, namely:
  - Have a significant corpus of books that is used for an autocomplete input;
  - Have a dropdown of existing books that the user picks from, with the bottom option being "create new book". This does not scale with larger amounts of books.
  - Expect users to always enter the exact information of the books the exact same way. This is almost impossible to defend or to verify, e.g. J.K. Rowling != JK Rowling. Doing a LIKE query on just Rowling would be too naive.
TODO: research feasibility.

- Where possible, class-based views will be used or at least extended from. There's something to be said for the control of FBV, but for the current requirements this really is overkill.

- I was initially going to hack the homepage into one of the two other apps for this project, but it doesn't feel right so I created a dedicated pages app for it for now. Future-proof to, for example, add about and privacy pages later.
