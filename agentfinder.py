def agent_finder(agent_url): 
    if agent_url == 'https://titles.trackercdn.com/valorant-api/agents/8e253930-4c05-31dd-1b6c-968525494517/displayicon.png':
        return "Omen"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/bb2a4828-46eb-8cd1-e765-15848195d751/displayicon.png':
        return "Neon"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/eb93336a-449b-9c1b-0a54-a891f7921d69/displayicon.png':
        return "Phoenix"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/displayicon.png':
        return "Jett"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/22697a3d-45bf-8dd7-4fec-84a9e28c69d7/displayicon.png':
        return "Chamber"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/9f0d8ba9-4140-b941-57d3-a7ad57c6b417/displayicon.png':
        return "Brimstone"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/569fdd95-4d10-43ab-ca70-79becc718b46/displayicon.png':
        return "Sage"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/601dbbe7-43ce-be57-2a40-4abd24953621/displayicon.png':
        return "Kayo"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/displayicon.png':
        return "Sova"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/a3bfb853-43b2-7238-a4f1-ad90e9e46bcc/displayicon.png':
        return "Reyna"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/41fb69c1-4189-7b37-f117-bcaf1e96f1bf/displayicon.png':
        return "Astra"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/1e58de9c-4950-5125-93e9-a0aee9f98746/displayicon.png':
        return "Killjoy"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/6f2a04ca-43e0-be17-7f36-b3908627744d/displayicon.png':
        return "Skye"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/f94c3b30-42be-e959-889c-5aa313dba261/displayicon.png':
        return "Raze"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/707eab51-4836-f488-046a-cda6bf494859/displayicon.png':
        return "Viper"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/7f94d92c-4234-0a36-9646-3a87eb8b5c89/displayicon.png':
        return "Yoru"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/5f8d3a7f-467b-97f3-062c-13acf203c006/displayicon.png':
        return "Breach"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/117ed9e3-49f3-6512-3ccf-0cada7e3823b/displayicon.png':
        return "Cypher"
    elif agent_url == "https://titles.trackercdn.com/valorant-api/agents/dade69b4-4f5a-8528-247b-219e5a1facd6/displayicon.png":
        return "Fade"
    else:
        return "unknown agent"

def class_finder(agent_url):
    if agent_url == 'https://titles.trackercdn.com/valorant-api/agents/8e253930-4c05-31dd-1b6c-968525494517/displayicon.png':
        return "Controller"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/bb2a4828-46eb-8cd1-e765-15848195d751/displayicon.png':
        return "Duelist"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/eb93336a-449b-9c1b-0a54-a891f7921d69/displayicon.png':
        return "Duelist"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/add6443a-41bd-e414-f6ad-e58d267f4e95/displayicon.png':
        return "Duelist"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/22697a3d-45bf-8dd7-4fec-84a9e28c69d7/displayicon.png':
        return "Sentinel"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/9f0d8ba9-4140-b941-57d3-a7ad57c6b417/displayicon.png':
        return "Controller"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/569fdd95-4d10-43ab-ca70-79becc718b46/displayicon.png':
        return "Sentinel"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/601dbbe7-43ce-be57-2a40-4abd24953621/displayicon.png':
        return "Initiator"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/320b2a48-4d9b-a075-30f1-1f93a9b638fa/displayicon.png':
        return "Initiator"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/a3bfb853-43b2-7238-a4f1-ad90e9e46bcc/displayicon.png':
        return "Duelist"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/41fb69c1-4189-7b37-f117-bcaf1e96f1bf/displayicon.png':
        return "Controller"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/1e58de9c-4950-5125-93e9-a0aee9f98746/displayicon.png':
        return "Sentinel"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/6f2a04ca-43e0-be17-7f36-b3908627744d/displayicon.png':
        return "Initiator"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/f94c3b30-42be-e959-889c-5aa313dba261/displayicon.png':
        return "Duelist"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/707eab51-4836-f488-046a-cda6bf494859/displayicon.png':
        return "Controller"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/7f94d92c-4234-0a36-9646-3a87eb8b5c89/displayicon.png':
        return "Duelist"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/5f8d3a7f-467b-97f3-062c-13acf203c006/displayicon.png':
        return "Initiator"
    elif agent_url == 'https://titles.trackercdn.com/valorant-api/agents/117ed9e3-49f3-6512-3ccf-0cada7e3823b/displayicon.png':
        return "Sentinel"
    elif agent_url == "https://titles.trackercdn.com/valorant-api/agents/dade69b4-4f5a-8528-247b-219e5a1facd6/displayicon.png":
        return "Initiator"
    else:
        return "unknown class"