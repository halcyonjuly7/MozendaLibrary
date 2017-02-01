import sqlite3

db = sqlite3.connect(':memory:')
cur = db.cursor()

class Server:    
      
    def __init__(self, name, apiKey):
        self.name = name
        self.apiKey = apiKey

    def GetServerUrl(self):
        url = ""
        url += "http://" + self.name + "/rest?WebServiceKey=" + self.apiKey + "&Service=Mozenda10&Operation="
        return url
  
    def ListOfApiNames(self):
        apiNames = ['Agent.Add','Agent.Delete','Agent.Get','Agent.GetCombinedCollections','Agent.GetJobs','Agent.GetList','Agent.Run',

                    'Collection.Add', 'Collection.AddField', 'Collection.AddItem', 'Collection.Clear', 'Collection.Delete', 'Collection.DeleteField',
                    'Collection.DeleteItem','Collection.GetFields','Collection.GetList','Collection.GetPublisher', 'Collection.GetViews', 'Collection.Publish'
                    'Collection.SetPublisher', 'Collection.SetUniqueFields', 'Collection.UpdateField', 'Collection.UpdateItem',

                    'Job.Cancel', 'Job.Get', 'Job.GetAgentProgress', 'Job.GetList', 'Job.Pause', 'Job.Resume',
                    
                    'View.DeleteItems', 'View.GetItems', 'View.SetFields'                                      
                    ]
        return apiNames

    def init_parameterTable(self):
        cur.execute('''CREATE TABLE parameterTable (
            name Text,
            api Text,
            parameterType Text
            )''')

        parameters = [('Name', 'Agent.Add', 'Required'),
                      ('Definition', 'Agent.Add','Required'),
                      ('Description', 'Agent.Add', 'Optional'),
                      ('BrowserIsolation', 'Agent.Add', 'Optional'),

                      ('AgentID','Agent.Delete','Required'),

                      ('AgentID','Agent.Get', 'Required'),

                      ('AgentID','Agent.GetCombinedCollections','Required'),

                      ('AgentID','Agent.GetJobs','Required'),
                      ('Job.Created','Agent.GetJobs','Optional'),
                      ('Job.Started','Agent.GetJobs','Optional'),
                      ('Job.Ended','Agent.GetJobs','Optional'),
                      ('Job.State','Agent.GetJobs','Optional'),

                      ('IncludeStartingURL','Agent.GetList','Optional'),

                      ('AgentID','Agent.Run','Required'),

                      ('Description','Collection.Add','Optional'),
                      
                      ('CollectionID','Collection.AddField','Required'),
                      ('Name', 'Collection.AddField', 'Required'),
                      ('Description', 'Collection.AddField', 'Optional'),

                      ('CollectionID', 'Collection.AddItem', 'Required'),
                      
                      ('CollectionID', 'Collection.Clear', 'Required'),
                      ('DeleteFilePackages', 'Collection.Clear', 'Optional'),

                      ('CollectionID', 'Collection.Delete','Required'),
                      
                      ('CollectionID', 'Collection.DeleteField', 'Required'),
                      ('Field', 'Collection.DeleteField', 'Required'),

                      ('CollectionID', 'Collection.DeleteItem', 'Required'),
                      ('ItemID', 'Collection.DeleteItem', 'Required'),

                      ('CollectionID', 'Collection.GetFields', 'Required'),
                      ('Include', 'Collection.GetFields', 'Optional'),

                      ('CollectionID', 'Collection.GetPublisher', 'Required'),

                      ('CollectionID', 'Collection.Publish', 'Required'),

                      ('CollectionID', 'Collection.SetPublisher', 'Required'),
                      ('Method', 'Collection.SetPublisher', 'Required'),
                      ('ViewID', 'Collection.SetPublisher', 'Optional'),
                      ('FileFormat', 'Collection.SetPublisher', 'Optional'),
                      ('FileName', 'Collection.SetPublisher', 'Optional'),
                      ('FileIncludeHeader', 'Collection.SetPublisher', 'Optional'),
                      ('PublishWhenAgentCompletes', 'Collection.SetPublisher', 'Optional'),
                      ('ItemStatusIncludeColumn', 'Collection.SetPublisher', 'Optional'),
                      ('ItemStatusIncludeAdded', 'Collection.SetPublisher', 'Optional'),
                      ('ItemStatusIncludeUnchanged', 'Collection.SetPublisher', 'Optional'),
                      ('ItemStatusIncludeDeleted', 'Collection.SetPublisher', 'Optional'),

                      ('CollectionID', 'Collection.SetUniqueFields', 'Required'),
                      ('Fields', 'Collection.SetUniqueFields', 'Required'),
                      
                      ('FieldID', 'Collection.UpdateField', 'Required'),
                      ('Description', 'Collection.UpdateField', 'Optional'),
                      ('Format', 'Collection.UpdateField', 'Optional'),
                      ('Name', 'Collection.UpdateField', 'Optional'),

                      ('CollectionID', 'Collection.UpdateItem', 'Required'),
                      ('ItemID', 'Collection.UpdateItem', 'Required'),

                      ('JobID', 'Job.Cancel', 'Required'),
                      
                      ('JobID', 'Job.Get', 'Required'),
                      ('IncludeJobStatistics', 'Job.Get', 'Optional'),
                      
                      ('JobID', 'Job.GetAgentProgress', 'Required'),

                      ('Job.Created', 'Job.GetList', 'Optional'),
                      ('Job.Started', 'Job.GetList', 'Optional'),
                      ('Job.Ended', 'Job.GetList', 'Optional'),
                      ('Job.State', 'Job.GetList', 'Optional'),
                      
                      ('JobID', 'Job.Pause', 'Required'),
                      
                      ('JobID', 'Job.Resume', 'Required'),
                      
                      ('ViewID', 'View.DeleteItems', 'Required'),
                      
                      ('ViewID', 'View.GetItems', 'Required'),
                      ('CollectionID', 'View.GetItems', 'Conditional'),
                      ('ItemStatusIncludeColumn', 'View.GetItems', 'Optional'),
                      ('PageNumber', 'View.GetItems', 'Optional'),
                      ('PageItemCount', 'View.GetItems', 'Optional'),
                      ('ViewParameter.JobID', 'View.GetItems', 'Optional'),
                      ('ViewParameter.', 'View.GetItems', 'Optional'),
                      ('ItemStatusIncludeAdded', 'View.GetItems', 'Optional'),
                      ('ItemStatusIncludeChanged', 'View.GetItems', 'Optional'),
                      ('ItemStatusIncludeUnchanged', 'View.GetItems', 'Optional'),
                      ('ItemStatusIncludeDeleted', 'View.GetItems', 'Optional'),
                      ('ItemStatusRangeStart', 'View.GetItems', 'Optional'),
                      ('ItemStatusRangeEnd', 'View.GetItems', 'Optional'),

                      ('ViewID', 'View.SetFields', 'Required'),
                      ('Fields', 'View.SetFields', 'Required'),
                      

                      ]

        cur.executemany('INSERT INTO parameterTable VALUES (?,?,?)', parameters)

    def select_parameterTable(self):
        for row in cur.execute("SELECT * FROM parameterTable WHERE api = 'View.GetItems'"):
            print(row)

    def select_sql(self,query):
        result = []
        for row in cur.execute(query):
            result.append(row)
        return result
       








x = Server("sup","bro")
x.init_parameterTable()
print(x.select_sql("SELECT * FROM parameterTable WHERE api = 'View.GetItems'"))



    









