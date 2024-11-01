class TrainingCourse:
    def __init__(self,title,duration,price_per_person):
        self.title = title
        self.duration = duration
        self.price_per_person = price_per_person
        self.delegates = []
    
    def add_delegate(self,delegate_name):
        self.delegates.append(delegate_name)

    def get_total_revenue(self):

        total_revenue = len(self.delegates)* self.price_per_person
        return total_revenue

if __name__ == "__main__" 
python1=TrainingCourse("python1",4,1600)
python1.add_delegate ("Akheela")
python1.add_delegate ("Edwin")

print(python1.get_total_revenue())