class FinanceRecord:
    def __init__(self, record_id, amount, category, date, description):
        self.id = record_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        return FinanceRecord(
            record_id=data["id"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data["description"]
        )
