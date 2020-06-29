class A:
    @staticmethod
    def show_static():
        print('static method')

    @classmethod
    def show_class(cls):
        print('class method')

    def show(self):
        print('bound method')


class B(A):
    @staticmethod
    def show_static():
        # super() here is super(__class__, ?)
        # this should fail
        super().show_static()

    @classmethod
    def show_class(cls):
        super().show_class()
        super().show_static()
        # super() here is super(__class__, cls) so the result is unbound
        # this should fail
        #super().show()

    def show(self):
        # super() here is super(__class__, self) so the result is bound
        super().show_class()
        super().show_static()
        super().show()
        

b = B()
#b.show()
#B.show_class()
#B.show_static()