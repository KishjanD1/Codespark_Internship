class user :
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email

class plans :
    def __init__(self,p_id,p_name,p_price):
        self.p_id =p_id
        self.p_name =p_name
        self.p_price = p_price

class subscriptions :
    def __init__(self, user_id, plan_id, start_date, end_date, status):
        self.user_id = user_id
        self.plan_id = plan_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

class coupons :
    def __init__(self, invoice_id, amount, status, retry_count):
        self.invoice_id = invoice_id
        self.amount = amount
        self.status = status
        self.retry_count = retry_count

class invoice :
    def __init__(self, invoice_id, user_id, amount, invoice_date, status):
        self.invoice_id = invoice_id
        self.user_id = user_id
        self.amount = amount
        self.invoice_date = invoice_date
        self.status = status