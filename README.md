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

"Futures" are accounts / portfolios at some time in the future, tied to accounts at a given time

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

#### Functions and Modules

##### I/O Module [io_firecal]

- Display Account
- Display Accounts
- Add Account
- Edit Account
- Delete Account
- Generate Future
- Modify Future
- Delete Future

##### Logic Module [logic_firecal]

- Getters and Setters 
- Account, Investment, Composition and Future Structs [Account, Future, Investment, Composition]
(An investment is a certain stock or indice. A coposition adds a % value to represent the proportion of an account's value invested in this.)
- Init Function for Account and Future [new]
- Edit Account Function (Uses Setters) [edit_account]
- Retrieve Account Function (Uses Getters) [retrieve_account]
- Delete Account Function [delete_account]
- Generate Future Function (Uses Init) [future]
- Retrieve Future Function (Uses Getters) [retrieve_future]
- Modify Future Function (Uses Setters) [modify_future]
- Delete Future Function [delete_future]

- ##### Account Struct

- name: String
- mut composition: [Composition; X]
- creation: Option(DateTime, None)

- ##### Future Struct

- name: String
- maturity: u8
- date: DateTime

- ##### Investment Struct

- name: String
- expected_return: u8

- ##### Composition Struct

- investment: Investment
- percentage: f32
