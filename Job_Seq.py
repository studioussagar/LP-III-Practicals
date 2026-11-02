def seq_job(x_list):

    # Find maximum deadline
    max_deadline = max(job[1] for job in x_list)

    # Create empty time slots
    slots = [None] * max_deadline

    # Sort jobs by profit
    x_list.sort(key=lambda x: x[2], reverse=True)

    total_profit = 0

    # Schedule jobs in available slots
    for j_id, deadline, profit in x_list:

        # Find the latest free slot
        for i in range(deadline - 1, -1, -1):

            if slots[i] is None:
                slots[i] = j_id
                total_profit += profit
                break

    # Return scheduled jobs and profit
    return [job for job in slots if job is not None], total_profit

# Accept number of jobs
a = int(input("Enter Number of Jobs: "))

jobs = []

# Accept job details
for i in range(a):
    j_id = input("Enter Job ID: ")
    deadline = int(input("Enter Job Deadline: "))
    profit = int(input("Enter Profit of the Job: "))

    # Store job details
    jobs.append((j_id, deadline, profit))


# Call the function
scheduled_jobs, z = seq_job(jobs)

# Display the result
print("\nScheduled Jobs:", scheduled_jobs)
print("Maximum Profit:", z)