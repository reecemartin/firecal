FIRE or "Financial Independence Retire Early" is an interesting lifestyle where one tries to maximize their savings and grow a signficiant
enough investment portfolio that they can live off of it (or reduce their working hours significantly). Trying to achieve FIRE involves
various recurring calculations, so it seems sensible to try to create a command line application which can automate and assist in these
routine calculations.

Some example tasks to simplify:

- Calculate annual investment returns
- Generate year by year returns for a given account given an investment (savings) and return rate
- Generate year by year returns for an entire portfolio of accounts
- Determine the time needed to reach a certain level of annual investment returns

### Design

#### Features

- Purchase comparator which allows you to compare two product options - say a razor and electric trimmer, with base and recurring costs to see which is less expensive and over what period of time

###### Out of Scope

#### Architecture

High Level Architecture, Database / How to Persists, What is frontend and backend responsible for (what functionality) - frontend input output and parsing, backend has API

What is the API - what functions?

Data model / How to represent data in code

#### User Flow

User opens application in their CLI, they then proceeed to enter their accounts which include names, current values, and expected return rate (ExRR) (+User Can Open Saved Accounts,
accounts have a recurring savings field).

Once a set of accounts are entered they can be deleted, edited / updated, and additional accounts can be added (+User Can Save Their Accounts).

Users can then generate future account value projections using planned recurring savings values and a set period of time, or date. (+User Can use existing recurring savings field).

Application generates future account values, a table of values each year, and the projected value at finish for each account and the portfolio (+User can also get +/-10% projections).

##### Extras

- Have information on each "page" clear the terminal so it feels more like a proper user interface.
- Consider tax rates, and taxed vs. untaxed accounts and "real" value.
- Have a feature to compare prices of products given a beginning price, and a set of recurring costs along with recurrence periods, let us calculate the long term costs and the break even points.
