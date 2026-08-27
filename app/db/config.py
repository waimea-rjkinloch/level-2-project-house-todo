#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------
class TopicTable:

    NAME = "topic"

    SCHEMA = """
        CREATE TABLE topic (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT NOT NULL,
            members TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO topic (name, members)
        VALUES
            ("Cleaning", "Chris, Sue")
            ("Cooking", "Robbie, Sue")
            ("Casual", "Robbie, Sue, Jack")
            ("Outdoors", "Jack, Chris")
    """

class TaskTable:

    NAME = "task"

    SCHEMA = """
        CREATE TABLE task (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id      INTEGER SECONDARY KEY,
            name          TEXT NOT NULL,
            description   TEXT,
            est_time      TEXT NOT NULL,
            complete_by   TEXT NOT NULL,
            urgency       INTEGER
        )
    """

    SEED_DATA = """
        INSERT INTO task (topic_id, name, description, est_time, complete_by, urgency)
        VALUES
            (1, "Vacuum lounge", "Make sure to charge after use", "10 minutes", "20th of August", 5),
            (2, "Cook dinner", "Pick from butter chicken or steak", "Varied", "7pm 19th of August", 9),
            (3, "Feed the cats", "Only feed Tiger a little bit", "1 minute", "7am 18th of August", 8),
            (4, "Mow the lawn", "Empty after use", "30 minutes", "23rd of August", 6)
    """

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    TopicTable,
    TaskTable
    # Add more tables here...
]

