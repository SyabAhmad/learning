"""
Data Model.
Handles generic data objects within the backend system.
"""

# Example: from sqlalchemy import Column, Integer, String
# Data Model Template.
# Defines the structure for storing and managing application data.

# class Data(Base):
#     __tablename__ = 'data'
#     id = Column(Integer, primary_key=True)
#     value = Column(String, nullable=False)
#     # Add more fields and methods as needed

class Data:
    """Represents a data entity."""
    
    def __init__(self, key, value):
        """
        Initialize a new Data instance.
        
        Args:
            key (str): Identifier for the data.
            value (any): The actual data content.
        """
        self.key = key
        self.value = value

    def __repr__(self):
        return f"<Data {self.key}>"

