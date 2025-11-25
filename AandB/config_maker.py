with open("config.yml","a+") as file:
    for i in range(1,26):
        file.write(f"AandB{i}.in:\n")
        file.write(f"  timeLimit: 1000\n")
        file.write(f"  memoryLimit: 524288\n")
        file.write(f"  score: 5\n")
        file.write(f"  subtaskId: {(i-1)//5+1}\n")
    
