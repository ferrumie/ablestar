## High Memory Usage
If i notice that memory usage on some Docker containers occasionally spikes these are the steps i will take
- I will check up the django app for possible memory leaks, check requests or processes running on Django server at the time the memory spike occurs and attempt optimizations.
- If DEBUG is turned on:
   -  Django keeps a list of all the SQL queries it makes and this continually grows
   - Might help to clear this once in while using `django.db.reset_queries()`
   - if the memory spike would'nt stop, then checking up for other optimaztion tricks might do the job, like optimizing data queries like using prefetch and prefetch_related with foreign key and m2m lookups
- If Celery is being used:
    - Check if the spikes occurs when tasks are being ran.
    - Reducing the amount of objects stored in memory at a point in time will reduce memory footprint.
- There may be an app creating huge amounts of logs on the filesystem constantly or a process loading an extremely huge queryset to memory. these should be checked and cleared
- I will check up the containers control group ( cgroup ) to track the consumption of the processes `cat /sys/fs/cgroup/memory/docker/<full container id>/memory.stat`
- After checking up the containers and noting the ones that occasional spikes and the memory they use, i will stress test the container memory usage
- Check up if logs and other static files are being stored in the containers and prune them if they are

- I will run `docker stats` to confirm what containers are taking up memory, and the amount of memory it takes.
- 
- If container memory limit has not been set, I will set up memory and CPU limits, this can prevent the containers from using all the available memories and affecting the rest. 
```
    docker run --cpus=2 -m 512m
```
