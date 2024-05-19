# SQL injection cheat sheet
#OSCP/WEB/PORTSWIGGER/LearningPath/ServerSide/SQLINJECTION

![](SQL%20injection%20cheat%20sheet/black-green-cheat-sheet-stamp-black-green-cheat-sheet-stamp-illustration-graphic-concept-108947651.jpg.webp)

This **SQL injection** cheat sheet contains examples of useful syntax that you can use to perform a variety of tasks that often arise when performing SQL injection attacks.

## String concatenation

You can concatenate together multiple strings to make a single string.

| Oracle         | =='foo'\|\|'bar'==                                           |
|:--------------:|:------------------------------------------------------------:|
| **Microsoft**  | =='foo'+'bar'==                                              |
| **PostgreSQL** | =='foo'\|\|'bar'==                                           |
| **MySQL**      | =='foo' 'bar'== [Note the space between the two strings]<br>==CONCAT('foo','bar')== |
## Substring

You can extract part of a string, from a specified offset with a specified length. Note that the offset index is 1-based. Each of the following expressions will return the string ==ba==.

| Oracle         | ==SUBSTR('foobar', 4, 2)==    |
|:--------------:|:-----------------------------:|
| **Microsoft**  | ==SUBSTRING('foobar', 4, 2)== |
| **PostgreSQL** | ==SUBSTRING('foobar', 4, 2)== |
| **MySQL**      | ==SUBSTRING('foobar', 4, 2)== |

## Comments

You can use comments to truncate a query and remove the portion of the original query that follows your input.

| Oracle         | ==--comment==                                          |
|:--------------:|:------------------------------------------------------:|
| **Microsoft**  | ==/\*comment\*/==                                      |
| **PostgreSQL** | ==\#comment==                                          |
| **MySQL**      | ==-- comment==  [Note the space after the double dash] |

## Database version

You can query the database to determine its type and version. This information is useful when formulating more complicated attacks.

| Oracle         | ==SELECT banner FROM v$version==<br>==SELECT version FROM v$instance== |
|:--------------:|:------------------------------------------------------------:|
| **Microsoft**  | ==SELECT @@version==                                         |
| **PostgreSQL** | ==SELECT version()==                                         |
| **MySQL**      | ==SELECT @@version==                                         |

## Database contents

You can list the tables that exist in the database, and the columns that those tables contain.

| Oracle         | ==SELECT banner FROM v$version==<br>==SELECT version FROM v$instance== |
|:--------------:|:------------------------------------------------------------:|
| **Microsoft**  | ==SELECT @@version==                                         |
| **PostgreSQL** | ==SELECT version()==                                         |
| **MySQL**      | ==SELECT @@version==                                         |