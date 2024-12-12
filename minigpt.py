import random

nepal_knowledge = {
    "capital": "Kathmandu",
    "population": "Approximately 30 million",
    "currency": "Nepalese Rupee (NPR)",
    "official language": "Nepali",
    "major religion": "Hinduism (with significant Buddhist influence)",
    "highest mountain": "Mount Everest",
    "national animal": "Cow",
    "national bird": "Himalayan Monal",
    "famous for": ["mountains", "trekking", "temples", "cultural diversity"],
    "major cities": ["Kathmandu", "Pokhara", "Lalitpur", "Bharatpur"],
    "border countries": ["China", "India"],
    "government type": "Federal Parliamentary Republic",
    "weather":"Varies based on altitude, from subtropical to alpine",
    "things to do":"Hiking, visiting temples, exploring cultural heritage, rafting",
    "food":"Dal Bhat, Momo, Thukpa",
    "festivals":["Dashain","Tihar", "Holi"],
    "national flower": "Rhododendron",
    "national sport": "Volleyball",
    "longest river": "Karnali River",
     "largest lake": "Phewa Lake",
    "UNESCO world heritage sites" : ["Sagarmatha National Park", "Kathmandu Valley", "Lumbini", "Chitwan National Park"],
    "major ethnic groups": ["Chhetri", "Brahmin", "Magar", "Tharu", "Tamang", "Newar"],
     "major airports" : ["Tribhuvan International Airport (Kathmandu)"],
    "typical house": "Brick or stone, often with sloping roofs",
    "traditional clothing" : ["Daura-Suruwal (men)", "Choli and Saree or Kurta-Salwar (women)"],
    "major industries": ["Tourism", "Agriculture", "Handicrafts", "Hydropower"],
     "historical kingdoms" : ["Malla Kingdom", "Shah Dynasty"],
    "traditional music": ["Nepali folk music", "Newari music"],
    "common greetings": ["Namaste", "Namaskar"],
    "major exports": ["Carpets", "Textiles", "Handicrafts", "Leather Goods"],
    "major imports": ["Petroleum Products", "Machinery", "Electronics", "Food"],
    "electricity": "230V, 50Hz",
    "driving side": "Left",
    "time zone": "Nepal Time (UTC+5:45)",
    "phone code": "+977",
    "independence day":"September 20",
    "founding date":"December 21, 1768",
     "mountains other than Everest": ["Annapurna", "Manaslu", "Dhaulagiri","Kangchenjunga"],
    "popular treks": ["Annapurna Base Camp Trek", "Everest Base Camp Trek", "Langtang Trek", "Ghorepani Poon Hill Trek"],
     "national parks":["Sagarmatha National Park", "Chitwan National Park", "Langtang National Park", "Bardiya National Park","Rara National Park"],
    "wildlife": ["Bengal tiger", "One-horned rhinoceros", "Snow leopard", "Red panda"],
    "important rivers":["Karnali River", "Koshi River", "Gandaki River"],
    "major passes": ["Thorong La Pass", "Laurebina Pass", "Cho La Pass"],
     "religious places":["Pashupatinath Temple", "Boudhanath Stupa", "Swoyambhunath Stupa", "Lumbini", "Muktinath Temple"],
      "historical places":["Kathmandu Durbar Square", "Patan Durbar Square", "Bhaktapur Durbar Square", "Nuwakot Durbar"],
      "types of tourism": ["Adventure Tourism", "Cultural Tourism", "Religious Tourism", "Eco-tourism"],
    "percentage of forest cover":"around 40%",
     "climate": "Monsoon, Summer, Winter, Autumn, Spring",
    "natural disasters": ["Earthquakes", "Floods", "Landslides"],
    "major crops" : ["Rice", "Maize", "Wheat", "Millet", "Potato"],
    "type of soil": "Alluvial, Mountainous, Loamy",
    "healthcare system":"Mostly private and limited public",
    "education system":"Primary, Secondary, Higher",
    "literacy rate":"Around 70%",
    "political parties":["Nepali Congress", "CPN (UML)", "CPN (Maoist Centre)"],
    "local government":"Municipalities, Rural Municipalities, Districts",
    "internet access": "Growing, but limited in rural areas",
    "media": ["Radio Nepal", "Nepal Television", "Various Newspapers"],
     "typical breakfast": ["Sel Roti", "Tea", "Chapatis"],
    "type of art":["Thangka painting", "Wood Carving", "Paubha painting"],
    "famous people":["Gautama Buddha", "Bhanubhakta Acharya", "Prithvi Narayan Shah"],
    "common spices":["Turmeric", "Cumin", "Coriander", "Chili"],
    "type of dance":["Lakhey Dance", "Deusi Bhailo", "Maruni Dance"],
    "local transportation":["Buses", "Taxis", "Tempos", "Motorcycles"],
     "shopping items":["Pashmina shawls", "Thangka paintings", "Khukuri knives", "Handicrafts"],
    "best time to visit":"October-November or March-April",
      "water sources": ["Rivers", "Streams", "Groundwater"],
    "problems": ["Poverty", "Corruption", "Political instability", "Natural disasters"],
     "how they celebrate new year":"Bisket Jatra",
     "national holidays": ["Republic Day", "Constitution Day", "Martyrs' Day"],
    "famous sweets":["Lal Mohan", "Jeri", "Barfi"],
    "common games":["Badminton", "Cricket", "Football", "Kabaddi"],
    "local markets":["Asan Market", "Indrachowk Market"],
    "handicrafts":"Hand-woven carpets, wooden masks, pottery",
    "types of agriculture":"Terrace farming and traditional farming",
      "major challenges":"Political and economic instability",
       "role of women":"Increasingly prominent in various fields",
        "major lakes":["Phewa lake", "Rara lake", "Tilicho lake"],
        "relationship with india":"Strong economic and cultural ties",
        "relationship with china":"Growing economic and political ties",
         "international organizations":"Member of United Nations",
          "health issues":"Malnutrition, infectious disease",
         "social problems":"Caste discrimination",
        "environmental issues":["Deforestation","Pollution"],
          "popular music genre":"Nepali Pop, Folk music",
        "the most common job": "Agriculture",
        "literacy rate of males":"Around 80%",
         "literacy rate of females":"Around 60%",
         "percentage of youth population":"Around 40%",
         "type of clothes people wear in summer":"Light cotton clothes",
          "type of clothes people wear in winter":"Woolen and warm clothes",
         "number of districts":"77",
          "name of the parliament": "Federal Parliament of Nepal",
          "name of the president":"Ram Chandra Paudel",
         "name of the prime minister":"Pushpa Kamal Dahal",
          "main source of income for nepal":"Agriculture, Tourism, Remittances",
        "major tourist destinations":["Kathmandu", "Pokhara", "Lumbini", "Chitwan", "Sagarmatha"],
        "type of roads":"Mostly narrow and winding",
       "average life expectancy":"Around 70 years",
        "type of school": ["Public Schools", "Private Schools", "Monasteries"],
         "different castes in nepal": ["Brahmin", "Chhetri", "Dalit", "Tharu", "Gurung"],
        "major sources of water pollution":["Industrial Waste", "Agricultural Runoff"],
         "how do people get water":"From Rivers, wells, and taps",
         "types of food people eat during festivals":["Sel Roti, Sweets, Farsan"],
          "how people celebrate holi": "With colors",
        "how people celebrate Dashain": "By flying kites, swing",
         "how people celebrate Tihar": "By lighting up house with diyo",
         "why do people visit temple": "To worship god",
        "types of medical centers in nepal": ["Hospital", "Health post", "Pharmacies"],
        "type of house people live in rural areas": "Mud and stone houses",
        "most common farming method":"Terrace farming",
        "what kind of electricity do people use":"Hydro electricity and solar power",
        "number of national park in nepal":"12",
        "types of plants in nepal":["Rhododendron", "Pine", "Oak", "Sal"],
        "types of animals in nepal":["Bengal tiger", "One-horned rhinoceros", "Snow leopard", "Red panda", "Gaur"],
        "how people travel in rural areas":"By foot, local buses, and motorcycles",
       "how people communicate": ["Nepali language", "Ethnic languages"],
         "main challenges for education": ["Access, Quality, Resources"],
        "main challenges for health": ["Access, Affordability, Quality"],
       "main problems faced by farmers":["Lack of irrigation, market access"],
       "main challenges in transport": ["Poor infrastructure, lack of maintenance"],
       "main challenges of tourism": ["Seasonal", "Infrastructure", "Sustainability"],
        "major causes of deforestation":["Illegal logging, agricultural expansion"],
        "main causes of pollution":["Vehicular emission", "Industrial waste", "Littering"],
        "traditional marriage system":["Arranged marriage", "Love marriage"],
       "types of music instrument":["Madal", "Sarangi", "Flute"],
       "types of poetry":["Folk poetry", "Modern poetry"],
       "common problems of youths":["Unemployment", "Drug Abuse"],
        "major exports of nepal":["Carpets", "Textiles", "Garments"],
        "main tourist season":["Autumn and spring"],
        "type of mountain in nepal":"Himalayan Mountains",
        "major industries in nepal":["Tourism", "Agriculture", "Hydropower"]
}

def nepal_chatbot(user_input):
    user_input = user_input.lower()

    if "capital" in user_input:
        return f"The capital of Nepal is {nepal_knowledge['capital']}."
    elif "population" in user_input:
        return f"The population of Nepal is approximately {nepal_knowledge['population']}."
    elif "currency" in user_input:
        return f"The currency of Nepal is {nepal_knowledge['currency']}."
    elif "language" in user_input:
        return f"The official language of Nepal is {nepal_knowledge['official language']}."
    elif "religion" in user_input:
      return f"The major religion in Nepal is {nepal_knowledge['major religion']}"
    elif "highest mountain" in user_input or "mount everest" in user_input:
        return f"The highest mountain in Nepal (and the world) is {nepal_knowledge['highest mountain']}."
    elif "national animal" in user_input:
      return f"The national animal of Nepal is the {nepal_knowledge['national animal']}"
    elif "national bird" in user_input:
      return f"The national bird of Nepal is the {nepal_knowledge['national bird']}"
    elif "famous for" in user_input:
       return f"Nepal is famous for {', '.join(nepal_knowledge['famous for'])}."
    elif "major cities" in user_input or "cities" in user_input:
        return f"Some major cities in Nepal include {', '.join(nepal_knowledge['major cities'])}."
    elif "border countries" in user_input or "borders" in user_input:
        return f"Nepal shares borders with {', and '.join(nepal_knowledge['border countries'])}."
    elif "government type" in user_input or "government" in user_input:
        return f"The government type in Nepal is a {nepal_knowledge['government type']}."
    elif "weather" in user_input:
      return f"The weather in Nepal {nepal_knowledge['weather']}."
    elif "things to do" in user_input or "activities" in user_input:
      return f"Some things you can do in Nepal include {', '.join(nepal_knowledge['things to do'])}."
    elif "food" in user_input:
       return f"Some popular food in Nepal include {', '.join(nepal_knowledge['food'])}."
    elif "festival" in user_input:
       return f"Some popular festivals in Nepal include {', '.join(nepal_knowledge['festivals'])}."
    elif "national flower" in user_input or "flower" in user_input:
       return f"The national flower of Nepal is {nepal_knowledge['national flower']}."
    elif "national sport" in user_input or "sport" in user_input:
         return f"The national sport of Nepal is {nepal_knowledge['national sport']}."
    elif "longest river" in user_input or "river" in user_input:
      return f"The longest river of Nepal is {nepal_knowledge['longest river']}."
    elif "largest lake" in user_input or "lake" in user_input:
      return f"The largest lake of Nepal is {nepal_knowledge['largest lake']}."
    elif "unesco world heritage" in user_input or "heritage sites" in user_input:
         return f"UNESCO World Heritage Sites in Nepal include {', '.join(nepal_knowledge['UNESCO world heritage sites'])}."
    elif "ethnic groups" in user_input or "ethnics" in user_input:
        return f"Major ethnic groups in Nepal are {', '.join(nepal_knowledge['major ethnic groups'])}."
    elif "major airports" in user_input or "airport" in user_input:
        return f"Major airports in Nepal include {', '.join(nepal_knowledge['major airports'])}."
    elif "typical house" in user_input or "house" in user_input:
       return f"A typical house in Nepal is {nepal_knowledge['typical house']}."
    elif "traditional clothing" in user_input or "dress" in user_input:
         return f"Traditional clothing in Nepal includes {', '.join(nepal_knowledge['traditional clothing'])}."
    elif "major industries" in user_input or "industry" in user_input:
         return f"Major industries in Nepal are {', '.join(nepal_knowledge['major industries'])}."
    elif "historical kingdoms" in user_input or "kingdom" in user_input:
          return f"Some historical kingdoms in Nepal include {', '.join(nepal_knowledge['historical kingdoms'])}."
    elif "traditional music" in user_input or "music" in user_input:
      return f"Traditional music in Nepal includes {', '.join(nepal_knowledge['traditional music'])}."
    elif "common greetings" in user_input or "greeting" in user_input:
      return f"Common greetings in Nepal include {', '.join(nepal_knowledge['common greetings'])}."
    elif "major exports" in user_input or "export" in user_input:
        return f"Major exports of Nepal are {', '.join(nepal_knowledge['major exports'])}."
    elif "major imports" in user_input or "import" in user_input:
      return f"Major imports of Nepal are {', '.join(nepal_knowledge['major imports'])}."
    elif "electricity" in user_input:
       return f"The electricity in Nepal is {nepal_knowledge['electricity']}."
    elif "driving side" in user_input:
      return f"In Nepal, you drive on the {nepal_knowledge['driving side']} side of the road."
    elif "time zone" in user_input:
        return f"The time zone in Nepal is {nepal_knowledge['time zone']}."
    elif "phone code" in user_input:
      return f"The phone code for Nepal is {nepal_knowledge['phone code']}."
    elif "independence day" in user_input or "independence" in user_input:
        return f"Nepal's independence day is {nepal_knowledge['independence day']}."
    elif "founding date" in user_input or "founded" in user_input:
       return f"Nepal's founding date is {nepal_knowledge['founding date']}."
    elif "mountains other than everest" in user_input or "other mountains" in user_input:
      return f"Mountains other than Mount Everest in Nepal include {', '.join(nepal_knowledge['mountains other than Everest'])}."
    elif "popular treks" in user_input or "trekking" in user_input:
         return f"Some popular treks in Nepal are {', '.join(nepal_knowledge['popular treks'])}."
    elif "national parks" in user_input or "park" in user_input:
       return f"National parks in Nepal include {', '.join(nepal_knowledge['national parks'])}."
    elif "wildlife" in user_input or "animals" in user_input:
      return f"Some wildlife found in Nepal include {', '.join(nepal_knowledge['wildlife'])}."
    elif "important rivers" in user_input:
       return f"Important rivers in Nepal include {', '.join(nepal_knowledge['important rivers'])}."
    elif "major passes" in user_input or "pass" in user_input:
       return f"Major passes in Nepal include {', '.join(nepal_knowledge['major passes'])}."
    elif "religious places" in user_input or "religious site" in user_input:
        return f"Some religious places in Nepal include {', '.join(nepal_knowledge['religious places'])}."
    elif "historical places" in user_input or "historical site" in user_input:
        return f"Some historical places in Nepal include {', '.join(nepal_knowledge['historical places'])}."
    elif "types of tourism" in user_input or "tourism type" in user_input:
         return f"Types of tourism in Nepal include {', '.join(nepal_knowledge['types of tourism'])}."
    elif "percentage of forest cover" in user_input or "forest cover" in user_input:
      return f"The percentage of forest cover in Nepal is around {nepal_knowledge['percentage of forest cover']}."
    elif "climate" in user_input:
       return f"The climate of Nepal includes {nepal_knowledge['climate']}."
    elif "natural disasters" in user_input or "disaster" in user_input:
      return f"Natural disasters that occur in Nepal include {', '.join(nepal_knowledge['natural disasters'])}."
    elif "major crops" in user_input or "crop" in user_input:
      return f"Major crops grown in Nepal are {', '.join(nepal_knowledge['major crops'])}."
    elif "type of soil" in user_input or "soil type" in user_input:
       return f"The soil in Nepal is mainly {nepal_knowledge['type of soil']}."
    elif "healthcare system" in user_input or "health care" in user_input:
      return f"The healthcare system in Nepal is {nepal_knowledge['healthcare system']}."
    elif "education system" in user_input or "education" in user_input:
        return f"The education system in Nepal includes {nepal_knowledge['education system']}."
    elif "literacy rate" in user_input or "literacy" in user_input:
      return f"The literacy rate of Nepal is {nepal_knowledge['literacy rate']}."
    elif "political parties" in user_input or "political party" in user_input:
      return f"Major political parties in Nepal include {', '.join(nepal_knowledge['political parties'])}."
    elif "local government" in user_input or "government level" in user_input:
        return f"The local government in Nepal is divided into {', '.join(nepal_knowledge['local government'])}."
    elif "internet access" in user_input or "internet" in user_input:
        return f"Internet access in Nepal is {nepal_knowledge['internet access']}."
    elif "media" in user_input:
       return f"Media in Nepal includes {', '.join(nepal_knowledge['media'])}."
    elif "typical breakfast" in user_input or "breakfast" in user_input:
        return f"A typical breakfast in Nepal includes {', '.join(nepal_knowledge['typical breakfast'])}."
    elif "type of art" in user_input or "art type" in user_input:
      return f"The types of art in Nepal are {', '.join(nepal_knowledge['type of art'])}."
    elif "famous people" in user_input or "famous person" in user_input:
      return f"Some famous people in Nepal include {', '.join(nepal_knowledge['famous people'])}."
    elif "common spices" in user_input or "spice" in user_input:
         return f"Common spices in Nepal include {', '.join(nepal_knowledge['common spices'])}."
    elif "type of dance" in user_input or "dance type" in user_input:
      return f"Types of dance in Nepal include {', '.join(nepal_knowledge['type of dance'])}."
    elif "local transportation" in user_input or "transportation" in user_input:
       return f"Local transportation in Nepal includes {', '.join(nepal_knowledge['local transportation'])}."
    elif "shopping items" in user_input or "shop" in user_input:
         return f"Popular shopping items in Nepal include {', '.join(nepal_knowledge['shopping items'])}."
    elif "best time to visit" in user_input or "best time" in user_input:
        return f"The best time to visit Nepal is {nepal_knowledge['best time to visit']}."
    elif "water sources" in user_input or "water source" in user_input:
      return f"The sources of water in Nepal are {', '.join(nepal_knowledge['water sources'])}."
    elif "problems" in user_input:
      return f"Some problems in Nepal include {', '.join(nepal_knowledge['problems'])}."
    elif "how they celebrate new year" in user_input or "new year celebration" in user_input:
       return f"They celebrate new year in Nepal by {nepal_knowledge['how they celebrate new year']}."
    elif "national holidays" in user_input or "holiday" in user_input:
        return f"Some national holidays of Nepal are {', '.join(nepal_knowledge['national holidays'])}."
    elif "famous sweets" in user_input or "sweet" in user_input:
       return f"Some famous sweets in Nepal include {', '.join(nepal_knowledge['famous sweets'])}."
    elif "common games" in user_input or "game" in user_input:
       return f"Common games played in Nepal include {', '.join(nepal_knowledge['common games'])}."
    elif "local markets" in user_input or "market" in user_input:
      return f"Some local markets in Nepal are {', '.join(nepal_knowledge['local markets'])}."
    elif "handicrafts" in user_input or "handicraft" in user_input:
        return f"Handicrafts of Nepal include {nepal_knowledge['handicrafts']}"
    elif "types of agriculture" in user_input or "agriculture type" in user_input:
      return f"Types of agriculture practiced in Nepal are {nepal_knowledge['types of agriculture']}."
    elif "major challenges" in user_input or "challenge" in user_input:
      return f"Major challenges faced by Nepal are {nepal_knowledge['major challenges']}."
    elif "role of women" in user_input or "women role" in user_input:
      return f"The role of women in Nepal is {nepal_knowledge['role of women']}."
    elif "major lakes" in user_input or "major lake" in user_input:
        return f"Major lakes in Nepal are {', '.join(nepal_knowledge['major lakes'])}."
    elif "relationship with india" in user_input or "india relation" in user_input:
       return f"Nepal has a {nepal_knowledge['relationship with india']}."
    elif "relationship with china" in user_input or "china relation" in user_input:
        return f"Nepal has a {nepal_knowledge['relationship with china']}."
    elif "international organizations" in user_input or "international organization" in user_input:
        return f"Nepal is a member of {nepal_knowledge['international organizations']}."
    elif "health issues" in user_input or "health problem" in user_input:
       return f"Major health issues in Nepal are {nepal_knowledge['health issues']}."
    elif "social problems" in user_input or "social issue" in user_input:
        return f"Social problems in Nepal include {nepal_knowledge['social problems']}."
    elif "environmental issues" in user_input or "environment" in user_input:
      return f"Environmental issues in Nepal are {', '.join(nepal_knowledge['environmental issues'])}."
    elif "popular music genre" in user_input or "music genre" in user_input:
      return f"A popular music genre in Nepal is {nepal_knowledge['popular music genre']}."
    elif "the most common job" in user_input or "common job" in user_input:
       return f"The most common job in Nepal is {nepal_knowledge['the most common job']}."
    elif "literacy rate of males" in user_input or "male literacy" in user_input:
      return f"The literacy rate of males in Nepal is {nepal_knowledge['literacy rate of males']}."
    elif "literacy rate of females" in user_input or "female literacy" in user_input:
      return f"The literacy rate of females in Nepal is {nepal_knowledge['literacy rate of females']}."
    elif "percentage of youth population" in user_input or "youth population" in user_input:
       return f"The percentage of the youth population in Nepal is {nepal_knowledge['percentage of youth population']}."
    elif "type of clothes people wear in summer" in user_input or "summer clothes" in user_input:
      return f"In summer, people in Nepal wear {nepal_knowledge['type of clothes people wear in summer']}."
    elif "type of clothes people wear in winter" in user_input or "winter clothes" in user_input:
      return f"In winter, people in Nepal wear {nepal_knowledge['type of clothes people wear in winter']}."
    elif "number of districts" in user_input or "district number" in user_input:
        return f"There are {nepal_knowledge['number of districts']} districts in Nepal."
    elif "name of the parliament" in user_input or "parliament name" in user_input:
       return f"The name of the parliament in Nepal is {nepal_knowledge['name of the parliament']}."
    elif "name of the president" in user_input or "president name" in user_input:
       return f"The president of Nepal is {nepal_knowledge['name of the president']}."
    elif "name of the prime minister" in user_input or "prime minister name" in user_input:
      return f"The prime minister of Nepal is {nepal_knowledge['name of the prime minister']}."
    elif "main source of income for nepal" in user_input or "income source" in user_input:
      return f"The main source of income for Nepal is {', '.join(nepal_knowledge['main source of income for nepal'])}."
    elif "major tourist destinations" in user_input or "major tourist place" in user_input:
        return f"Major tourist destinations in Nepal include {', '.join(nepal_knowledge['major tourist destinations'])}."
    elif "type of roads" in user_input or "road type" in user_input:
       return f"The type of roads in Nepal are {nepal_knowledge['type of roads']}."
    elif "average life expectancy" in user_input or "life expectancy" in user_input:
      return f"The average life expectancy in Nepal is {nepal_knowledge['average life expectancy']}."
    elif "type of school" in user_input or "school type" in user_input:
      return f"The types of schools in Nepal are {', '.join(nepal_knowledge['type of school'])}."
    elif "different castes in nepal" in user_input or "caste in nepal" in user_input:
       return f"Different castes in Nepal are {', '.join(nepal_knowledge['different castes in nepal'])}."
    elif "major sources of water pollution" in user_input or "water pollution source" in user_input:
       return f"Major sources of water pollution in Nepal are {', '.join(nepal_knowledge['major sources of water pollution'])}."
    elif "how do people get water" in user_input or "source of drinking water" in user_input:
      return f"People get their water in Nepal {nepal_knowledge['how do people get water']}."
    elif "types of food people eat during festivals" in user_input or "festival food" in user_input:
      return f"During festivals people eat {', '.join(nepal_knowledge['types of food people eat during festivals'])}."
    elif "how people celebrate holi" in user_input or "holi celebration" in user_input:
      return f"People celebrate Holi by {nepal_knowledge['how people celebrate holi']}."
    elif "how people celebrate Dashain" in user_input or "dashain celebration" in user_input:
      return f"People celebrate Dashain by {nepal_knowledge['how people celebrate Dashain']}."
    elif "how people celebrate Tihar" in user_input or "tihar celebration" in user_input:
       return f"People celebrate Tihar by {nepal_knowledge['how people celebrate Tihar']}."
    elif "why do people visit temple" in user_input or "temple visit" in user_input:
      return f"People visit temples in Nepal {nepal_knowledge['why do people visit temple']}."
    elif "types of medical centers in nepal" in user_input or "medical center type" in user_input:
      return f"The types of medical centers in Nepal are {', '.join(nepal_knowledge['types of medical centers in nepal'])}."
    elif "type of house people live in rural areas" in user_input or "rural house" in user_input:
      return f"People in rural areas live in {nepal_knowledge['type of house people live in rural areas']}."
    elif "most common farming method" in user_input or "farming method" in user_input:
        return f"The most common farming method in Nepal is {nepal_knowledge['most common farming method']}."
    elif "what kind of electricity do people use" in user_input or "type of electricity" in user_input:
         return f"People in Nepal use {nepal_knowledge['what kind of electricity do people use']}."
    elif "number of national park in nepal" in user_input or "national park number" in user_input:
        return f"There are {nepal_knowledge['number of national park in nepal']} national parks in Nepal."
    elif "types of plants in nepal" in user_input or "plant type" in user_input:
       return f"Types of plants in Nepal include {', '.join(nepal_knowledge['types of plants in nepal'])}."
    elif "types of animals in nepal" in user_input or "animal type" in user_input:
      return f"Types of animals in Nepal include {', '.join(nepal_knowledge['types of animals in nepal'])}."
    elif "how people travel in rural areas" in user_input or "rural travel" in user_input:
        return f"People travel in rural areas of Nepal by {', '.join(nepal_knowledge['how people travel in rural areas'])}."
    elif "how people communicate" in user_input or "communication method" in user_input:
       return f"People communicate in Nepal using {', '.join(nepal_knowledge['how people communicate'])}."
    elif "main challenges for education" in user_input or "education challenge" in user_input:
        return f"The main challenges for education in Nepal are {', '.join(nepal_knowledge['main challenges for education'])}."
    elif "main challenges for health" in user_input or "health challenge" in user_input:
      return f"The main challenges for health in Nepal are {', '.join(nepal_knowledge['main challenges for health'])}."
    elif "main problems faced by farmers" in user_input or "farmer problem" in user_input:
      return f"The main problems faced by farmers in Nepal are {', '.join(nepal_knowledge['main problems faced by farmers'])}."
    elif "main challenges in transport" in user_input or "transportation challenge" in user_input:
        return f"The main challenges in transport in Nepal are {', '.join(nepal_knowledge['main challenges in transport'])}."
    elif "main challenges of tourism" in user_input or "tourism challenge" in user_input:
      return f"The main challenges of tourism in Nepal are {', '.join(nepal_knowledge['main challenges of tourism'])}."
    elif "major causes of deforestation" in user_input or "deforestation cause" in user_input:
      return f"Major causes of deforestation in Nepal include {', '.join(nepal_knowledge['major causes of deforestation'])}."
    elif "main causes of pollution" in user_input or "pollution cause" in user_input:
        return f"Main causes of pollution in Nepal are {', '.join(nepal_knowledge['main causes of pollution'])}."
    elif "traditional marriage system" in user_input or "marriage system" in user_input:
       return f"The traditional marriage system in Nepal is {', '.join(nepal_knowledge['traditional marriage system'])}."
    elif "types of music instrument" in user_input or "music instrument" in user_input:
       return f"The types of music instrument in Nepal are {', '.join(nepal_knowledge['types of music instrument'])}."
    elif "types of poetry" in user_input or "poetry type" in user_input:
      return f"The types of poetry in Nepal are {', '.join(nepal_knowledge['types of poetry'])}."
    elif "common problems of youths" in user_input or "youth problem" in user_input:
        return f"The common problems faced by youths in Nepal are {', '.join(nepal_knowledge['common problems of youths'])}."
    elif "major exports of nepal" in user_input or "export" in user_input:
        return f"Major exports of Nepal include {', '.join(nepal_knowledge['major exports of nepal'])}."
    else:
        return "I'm not sure I understand. Please ask me a question about Nepal."
    
    # Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
      break
    response = nepal_chatbot(user_input)
    print("Chatbot:", response)