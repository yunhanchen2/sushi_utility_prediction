## Code Files Description

### Optimal Solution

1. **The plot of the original optimal solution (`original_graph.py`)**

   - **Description:**  
     This script plot the revenue on the primary data for the optimal solutions obtained from different sample sizes, given a specific sushi supply quantity k. 

     **Input:** number(k) of sushi provided to the custome; The axis start, end, and interval of the plot

     **Output:** a graph (also the optimal solution for each cases)
   - **Running Instruction:**  
     Run the script using:
     ```
     python3 original_graph.py
     ```
     After executing, the terminal will prompt:
     ```
     How many sushi do you want to serve customers? (not more than 10): 
     ```
     You can input a number like `1`, `2`, `3`, etc.
     To get the axis start, end, and interval of the plot, the terminal will prompt:
     ```
     Enter start value:  
     Enter end value (inclusive):    
     Enter step size:
     ```
     You can input a number like (`1`, `5000`, `1`), etc.

   - **Logic of the code:**
     ![Plot](images/code_logic1.png)
     
2. **0 shot LLM Generation (`gpt_persona_0_shot.py`)**

### 
