
##### Buggy Python Fixes

Below are the steps I used for fixing the buggy python challenge

- Test cases
- Comments
- Avoided DRY
- Consistency
- Utf-8
- Looping through integers
- Default arguments fix
- Using the right data type
- Fixed logical error


###### Test cases
I ran the `main.py` file to see the output
I read the error messages and also checked for the assertions that failed
I narrowed down to the codebase to understand what it's meant to do so as to fix them


###### Comments
I wrote some comments to enhance the readability of the codes


###### Avoided DRY
I created a function that returns the paid loans in an array because `calculate_paid_loans` and `average_paid_loans` functions have some repetition


###### Consistency
I used `.get` for getting access to the dictionary objects


###### UTF-8
I made the file executable in UTF-8 mode because of the emojis by adding `# -*- coding: UTF-8 -*-`


###### Looping through integers
Python does not support looping through integers without using `range` inbuilt function, I fixed the issue in `loop.py`


###### Default arguments fix
Functions are treated as `first-class objects` in python, default parameters are kind of "member data" and therefore their state may change from one call to the other - exactly as in any other object. I fixed the logical error there


###### Using the right data type
I ensured the right data type are used, `append` method is only available in `list` data type

###### Fixed logical error
I solved a logical issue that checks when the status is `unpaid` for `calculate_unpaid_loans`
