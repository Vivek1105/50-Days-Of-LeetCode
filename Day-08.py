# Problem - 1491. Average Salary Excluding the Minimum and Maximum Salary


from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        # Initialize min_salary and max_salary
        min_salary, max_salary = salary[0], salary[0]
        
        # Find the minimum and maximum salaries
        for s in salary:
            if s < min_salary:
                min_salary = s
            elif s > max_salary:
                max_salary = s
        
        # Calculate the sum of remaining salaries
        sum_salary = 0
        count = 0
        for s in salary:
            if s != min_salary and s != max_salary:
                sum_salary += s
                count += 1
        
        # Calculate and return the average
        return sum_salary / count
