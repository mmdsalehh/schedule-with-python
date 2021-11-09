from datetime import datetime
import time
import math
import subprocess

class Schedule:
    __allowed_type = ['command', 'reminder']
    
    def __init__(self):
        self.jobs = []
        
    def current_time(self):
        return datetime.now()
    
    def mainloop(self):
        try:
            while True:
                for job_index, job in enumerate(self.jobs):
                    current_time = self.current_time()
                    job_time = job['time']
                    if job_time <= current_time:
                        job_type = job['type']
                        if job_type == 'command':
                            for command in job['command']:
                                execute_command = self.execute_command(command)
                                self.show_output(execute_command)
                        elif job_type == 'reminder':
                            reminder_text = job['reminder_text']
                            self.show_output(reminder_text)
                        self.jobs.pop(job_index)
                        break
                if not self.jobs:
                    return
                time.sleep(self.get_nearest_time())
        except KeyboardInterrupt:
            pass
        
    def show_output(self, text):
        print(text)
        
    def execute_command(self, command):
        cmd = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        return output_byte.decode('utf-8')
        
    def add(self, job:dict):
        job_type = job.get('type', None)
        assert job_type in self.__allowed_type
        
        if job_type == 'command':
            assert job.get('command', None)
            
        elif job_type == 'reminder':
            assert job.get('reminder_text', None)
            
        self.jobs.append(job)
    
    def get_nearest_time(self):
        nearets_time = 1
        for job in self.jobs:
            job_time = job['time']
            current_time = self.current_time()
            if job_time > current_time:
                diffrence = job_time - current_time
                total_seconds = diffrence.total_seconds()
                if total_seconds < nearets_time:
                    nearets_time = total_seconds
            else:
                return 0
        return nearets_time
        
    def run(self):
        self.mainloop()
