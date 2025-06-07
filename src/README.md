## Code Files Description
### Data generation
1. **few shot LLM Generation (`full_few_shot.py`)**

   - **Description:**
     This script is few shot LLM Generation. The prompt can be change to generate 0-shot or no persona LLM data.
     
     **Input:** the number of sushi rankings to generate  
     **Output:** file called `sushi_ranking.txt` containing rankings, located in the same directory as `full_few_shot.py`

     An example of few-shot prompt:
     ```
     First, here is the background:
     Generally speaking, the eastern Japanese prefers more oily and more heavily seasoned food than the western Japanese.
     The western prefers to UDON noodle, while the eastern loves SOBA noodle.
     The way of cooking Kabayaki, grilled eels, is clearly different.
 
     The other preference patterns depending on regions are:
     The SUSHI in Tokyo is specially called Edomaezushi. The typical examples of the Edomae are: anago (ID:1), zuke (ID:76), and kohada (ID:23).
     A nattou (fermented bean) is loved in the Ibaraki prefecture, but is hated in the Kinki region.
     An oceanic bonito is frequently eaten in the Kochi prefecture.
     A mentaiko (chili cod roe) is a noted product in the Fukuoka prefecture.
     A karasumi (dried mullet roe) is a noted product in the Nagasaki prefecture.
     A batttera sushi is mainly eaten in the Kinki region.

     We already know some of the rankings correspond to personas:
     User 8295 is a female aged 20–29. They have spent most of their life in Aichi (Chukyo, Eastern Japan). Ranks the sushi as: 5 2 7 8 0 3 6 9 4 1
     User 5585 is a male aged 30–39. They have spent most of their life in Shizuoka (Kanto and Shizuoka, Eastern Japan). Ranks the sushi as: 7 2 3 0 5 4 8 1 6 9
     User 5091 is a male aged 20–29. They have spent most of their life in Mie (Chukyo, Eastern Japan). Ranks the sushi as: 5 0 7 2 3 6 8 9 1 4
     User 1631 is a male aged 40–49. They have spent most of their life in Tokyo (Kanto and Shizuoka, Eastern Japan). Ranks the sushi as: 4 5 7 1 2 3 8 6 9 0
     User 1978 is a female aged 30–39. They have spent most of their life in Osaka (Kinki, Western Japan). Ranks the sushi as: 0 3 6 5 2 9 1 8 7 4
     
     User profile:
     User 1234 is a female aged 20–29. They have spent most of their life in Tokyo (Kanto and Shizuoka, Eastern Japan).

     Sushi items:
     ebi (ID 0) is a non-maki type from the shrimp or crab group, belonging to the seafood category. It is light in taste, very frequently eaten, very commonly found in sushi restaurants, and has a price score of 1.84.
     anago (ID 1) is a non-maki type from the tare (eel sauce) group, belonging to the seafood category. It is heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.99.
     maguro (ID 2) is a non-maki type from the akami (red meat fish) group, belonging to the seafood category. It is moderate in taste, very frequently eaten, very commonly found in sushi restaurants, and has a price score of 1.87.
     ika (ID 3) is a non-maki type from the squid or octopus group, belonging to the seafood category. It is light in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.52.
     uni (ID 4) is a non-maki type from the other seafood group, belonging to the seafood category. It is heavy in taste, sometimes eaten, very commonly found in sushi restaurants, and has a price score of 3.29.
     ikura (ID 5) is a non-maki type from the roe group, belonging to the seafood category. It is heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 2.70.
     tamago (ID 6) is a non-maki type from the egg group, belonging to the non-seafood category. It is moderate in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 1.03.
     toro (ID 7) is a non-maki type from the akami (red meat fish) group, belonging to the seafood category. It is very heavy in taste, often eaten, very commonly found in sushi restaurants, and has a price score of 4.49.
     tekka_maki (ID 8) is a maki roll from the akami (red meat fish) group, belonging to the seafood category. It is moderate in taste, often eaten, occasionally found in sushi restaurants, and has a price score of 1.58.
     kappa_maki (ID 9) is a maki roll from the vegetable group, belonging to the non-seafood category. It is very light in taste, sometimes eaten, occasionally found in sushi restaurants, and has a price score of 1.02.

     Please simulate a sushi ranking this person would produce.
     Please avoid always ranking the same item first across people.
     Return exactly 10 unique integers from 0 to 9, in order of preference, like:
     3 1 7 2 5 0 8 9 4 6
     ```

   - **Running Instruction:**
      First get your OpenAI api:
     ```
     export OPENAI_API_KEY=sk-xxxxx...  (your api)
     ```
      Run the script using:
     ```
     python3 full_few_shot.py
     ```
     After executing, you can press Control C to stop the code when it already generate the amount that you want.
     
### Optimal Solution

1. **The plot of the optimal solution for a input file(`get_opt.py`)**

   - **Description:**  
     This script plot the revenue on the primary data for the optimal solutions obtained from different sample sizes in a file, given a specific sushi supply quantity k. 

     **Input:** The file name; The number(k) of sushi provided to the custome; The axis start, end, and interval of the plot

     **Output:** a graph (also the optimal solution for each cases)
     
   - **Running Instruction:**  
     Run the script using:
     ```
     python3 get_opt.py
     ```
     After executing, the terminal will prompt:
     ```
     Enter the filename:
     ```
     You can input a number like `5000_a.txt`, etc.
     
     Then, the terminal will prompt:
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
     ![Plot](../images/code_logic1.png)
     
     
2. **GPT comparation(`combine_smooth.py`)**
   - **Description:**  
     This compare the performance between GPT-4o and GPT-3.5-turbo, which draw the graph for no-persona, 0-shot and few shot for two GPT editions.

     **Input:** The number(k) of sushi provided to the custome

     **Output:** a graph (also the optimal solution for each cases)

   - **Running Instruction:**  
     Run the script using:
     ```
     python3 combine_smooth.py
     ```
     After executing, the terminal will prompt:
     ```
     How many sushi do you want to serve customers? (not more than 10): 
     ```
     You can input a number like `1`, `2`, `3`, etc.
   - **Logic of the code:**
     ![Plot](../images/code_logic2.png)
### 
