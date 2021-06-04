# Total time required to travel a path denoted by a given string

Given a string path consisting of characters ‘N’, ‘S’, ‘E’ and ‘W’ denoting 1 unit movement in North, South, East, and West directions respectively, the task is to find the time taken to travel the complete path starting from the origin, if it takes 2 and 1 minutes to travel on an unvisited and visited segment respectively.

### Example-1:
<br>
-Input: path = “NNES” <br>
-Output : 8 <br>
**- Explanation: **
- Since every segment is visited only once, cost = 2 * 4 = 8. <br>

### Example-2:
<br>
- Input : path = “NSE” <br>
- Output : 5 <br>
<br>
**- Explanation: ** <br>
- Step 1: Travel north. Time Taken = 2 minutes. <br>
- Step 2: Travel south on that same visited segment. Time Taken = 1 minutes. <br>
- Step 3: Travel east.Time Taken = 2 minutes. Therefore, total time taken = 2 + 1 + 2 = 5. <br>
