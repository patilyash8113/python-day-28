# python-day-28
Day 23 of my Python journey
Today i learn about map, filter, and reduce
(1) map=The map() function applies a given function to each item of an iterable and returns an iterator that yields the results.
Eg. suppose i have number list and create a funtion that square a x number 
now i create a New variable and variable have values like list and use map and map accept two conditions 1st function and second take iterable now i print that new variable and output is each number have square list ..

(2) filter = The filter() function constructs an iterator from elements of an iterable for which a function returns True . In other words, it filters the iterable based on a condition
Eg.suppose i create a function that is_grater_than_10 and that stores one argument X now i use if and else statement if x>9 return true and else return false now i create a number list and next i create a variable called "New" new stores filter and filter need two arguments 1st function and 2nd num variable now print num now output come only the numbers that are greater than 9 are printed on the list.

(3) reduce()=The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value. reduce is not a built-in function; it must be imported from the functools module.
Eg.lets understand it 
1st we need to import funtool fro internal module
now i create a function called sum that stores two arguments a and band returns a+b
now i create a number list that have multiple numbers and create variable use reduce () and reduce stores two arguments 1st function and second iterable now i print that "C".
now output looks like this
# numbers=[2,2,5,8,9,8]
# #       [4,5,8,9,8]
# #       [9,8,9,8]
# #       [17,9,8]
# #       [26,8]
# #       [34]
here first two numbers are sum together each and every stp  and create step by step process, now the output is 34
