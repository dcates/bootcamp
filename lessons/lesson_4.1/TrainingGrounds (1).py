
# coding: utf-8

# In[4]:


# Import Dependencies
import pandas as pd
import random


# In[5]:


# A gigantic DataFrame of individuals' names, their trainers, their weight, and their days as gym members
training_data = pd.DataFrame({
    "Name":["Gino Walker","Hiedi Wasser","Kerrie Wetzel","Elizabeth Sackett","Jack Mitten","Madalene Wayman","Jamee Horvath","Arlena Reddin","Tula Levan","Teisha Dreier","Leslie Carrier","Arlette Hartson","Romana Merkle","Heath Viviani","Andres Zimmer","Allyson Osman","Yadira Caggiano","Jeanmarie Friedrichs","Leann Ussery","Bee Mom","Pandora Charland","Karena Wooten","Elizabet Albanese","Augusta Borjas","Erma Yadon","Belia Lenser","Karmen Sancho","Edison Mannion","Sonja Hornsby","Morgan Frei","Florencio Murphy","Christoper Hertel","Thalia Stepney","Tarah Argento","Nicol Canfield","Pok Moretti","Barbera Stallings","Muoi Kelso","Cicely Ritz","Sid Demelo","Eura Langan","Vanita An","Frieda Fuhr","Ernest Fitzhenry","Ashlyn Tash","Melodi Mclendon","Rochell Leblanc","Jacqui Reasons","Freeda Mccroy","Vanna Runk","Florinda Milot","Cierra Lecompte","Nancey Kysar","Latasha Dalton","Charlyn Rinaldi","Erline Averett","Mariko Hillary","Rosalyn Trigg","Sherwood Brauer","Hortencia Olesen","Delana Kohut","Geoffrey Mcdade","Iona Delancey","Donnie Read","Cesar Bhatia","Evia Slate","Kaye Hugo","Denise Vento","Lang Kittle","Sherry Whittenberg","Jodi Bracero","Tamera Linneman","Katheryn Koelling","Tonia Shorty","Misha Baxley","Lisbeth Goering","Merle Ladwig","Tammie Omar","Jesusa Avilla","Alda Zabala","Junita Dogan","Jessia Anglin","Peggie Scranton","Dania Clodfelter","Janis Mccarthy","Edmund Galusha","Tonisha Posey","Arvilla Medley","Briana Barbour","Delfina Kiger","Nia Lenig","Ricarda Bulow","Odell Carson","Nydia Clonts","Andree Resendez","Daniela Puma","Sherill Paavola","Gilbert Bloomquist","Shanon Mach","Justin Bangert","Arden Hokanson","Evelyne Bridge","Hee Simek","Ward Deangelis","Jodie Childs","Janis Boehme","Beaulah Glowacki","Denver Stoneham","Tarra Vinton","Deborah Hummell","Ulysses Neil","Kathryn Marques","Rosanna Dake","Gavin Wheat","Tameka Stoke","Janella Clear","Kaye Ciriaco","Suk Bloxham","Gracia Whaley","Philomena Hemingway","Claudette Vaillancourt","Olevia Piche","Trey Chiles","Idalia Scardina","Jenine Tremble","Herbert Krider","Alycia Schrock","Miss Weibel","Pearlene Neidert","Kina Callender","Charlotte Skelley","Theodora Harrigan","Sydney Shreffler","Annamae Trinidad","Tobi Mumme","Rosia Elliot","Debbra Putt","Rena Delosantos","Genna Grennan","Nieves Huf","Berry Lugo","Ayana Verdugo","Joaquin Mazzei","Doris Harmon","Patience Poss","Magaret Zabel","Marylynn Hinojos","Earlene Marcantel","Yuki Evensen","Rema Gay","Delana Haak","Patricia Fetters","Vinnie Elrod","Octavia Bellew","Burma Revard","Lakenya Kato","Vinita Buchner","Sierra Margulies","Shae Funderburg","Jenae Groleau","Louetta Howie","Astrid Duffer","Caron Altizer","Kymberly Amavisca","Mohammad Diedrich","Thora Wrinkle","Bethel Wiemann","Patria Millet","Eldridge Burbach","Alyson Eddie","Zula Hanna","Devin Goodwin","Felipa Kirkwood","Kurtis Kempf","Kasey Lenart","Deena Blankenship","Kandra Wargo","Sherrie Cieslak","Ron Atha","Reggie Barreiro","Daria Saulter","Tandra Eastman","Donnell Lucious","Talisha Rosner","Emiko Bergh","Terresa Launius","Margy Hoobler","Marylou Stelling","Lavonne Justice","Kala Langstaff","China Truett","Louanne Dussault","Thomasena Samaniego","Charlesetta Tarbell","Fatimah Lade","Malisa Cantero","Florencia Litten","Francina Fraise","Patsy London","Deloris Mclaughlin"],
    "Trainer":['Bettyann Savory','Mariah Barberio','Gordon Perrine','Pa Dargan','Blanch Victoria','Aldo Byler','Aldo Byler','Williams Camire','Junie Ritenour','Gordon Perrine','Bettyann Savory','Mariah Barberio','Aldo Byler','Barton Stecklein','Bettyann Savory','Barton Stecklein','Gordon Perrine','Pa Dargan','Aldo Byler','Brittani Brin','Bettyann Savory','Phyliss Houk','Bettyann Savory','Junie Ritenour','Aldo Byler','Calvin North','Brittani Brin','Junie Ritenour','Blanch Victoria','Brittani Brin','Bettyann Savory','Blanch Victoria','Mariah Barberio','Bettyann Savory','Blanch Victoria','Brittani Brin','Junie Ritenour','Pa Dargan','Gordon Perrine','Phyliss Houk','Pa Dargan','Mariah Barberio','Phyliss Houk','Phyliss Houk','Calvin North','Williams Camire','Brittani Brin','Gordon Perrine','Bettyann Savory','Bettyann Savory','Pa Dargan','Phyliss Houk','Barton Stecklein','Blanch Victoria','Coleman Dunmire','Phyliss Houk','Blanch Victoria','Pa Dargan','Harland Coolidge','Calvin North','Bettyann Savory','Phyliss Houk','Bettyann Savory','Harland Coolidge','Gordon Perrine','Junie Ritenour','Harland Coolidge','Blanch Victoria','Mariah Barberio','Coleman Dunmire','Aldo Byler','Bettyann Savory','Gordon Perrine','Bettyann Savory','Barton Stecklein','Harland Coolidge','Aldo Byler','Aldo Byler','Pa Dargan','Junie Ritenour','Brittani Brin','Junie Ritenour','Gordon Perrine','Mariah Barberio','Mariah Barberio','Mariah Barberio','Bettyann Savory','Brittani Brin','Aldo Byler','Phyliss Houk','Blanch Victoria','Pa Dargan','Phyliss Houk','Brittani Brin','Barton Stecklein','Coleman Dunmire','Bettyann Savory','Bettyann Savory','Gordon Perrine','Blanch Victoria','Junie Ritenour','Phyliss Houk','Coleman Dunmire','Williams Camire','Harland Coolidge','Williams Camire','Aldo Byler','Harland Coolidge','Gordon Perrine','Brittani Brin','Coleman Dunmire','Calvin North','Phyliss Houk','Brittani Brin','Aldo Byler','Bettyann Savory','Brittani Brin','Gordon Perrine','Calvin North','Harland Coolidge','Coleman Dunmire','Harland Coolidge','Aldo Byler','Junie Ritenour','Blanch Victoria','Harland Coolidge','Blanch Victoria','Junie Ritenour','Harland Coolidge','Junie Ritenour','Gordon Perrine','Brittani Brin','Coleman Dunmire','Williams Camire','Junie Ritenour','Brittani Brin','Calvin North','Barton Stecklein','Barton Stecklein','Mariah Barberio','Coleman Dunmire','Bettyann Savory','Mariah Barberio','Pa Dargan','Barton Stecklein','Coleman Dunmire','Brittani Brin','Barton Stecklein','Pa Dargan','Barton Stecklein','Junie Ritenour','Bettyann Savory','Williams Camire','Pa Dargan','Calvin North','Williams Camire','Coleman Dunmire','Aldo Byler','Barton Stecklein','Coleman Dunmire','Blanch Victoria','Mariah Barberio','Mariah Barberio','Harland Coolidge','Barton Stecklein','Phyliss Houk','Pa Dargan','Bettyann Savory','Barton Stecklein','Harland Coolidge','Junie Ritenour','Pa Dargan','Mariah Barberio','Blanch Victoria','Williams Camire','Phyliss Houk','Phyliss Houk','Coleman Dunmire','Mariah Barberio','Gordon Perrine','Coleman Dunmire','Brittani Brin','Pa Dargan','Coleman Dunmire','Brittani Brin','Blanch Victoria','Coleman Dunmire','Gordon Perrine','Coleman Dunmire','Aldo Byler','Aldo Byler','Mariah Barberio','Williams Camire','Phyliss Houk','Aldo Byler','Williams Camire','Aldo Byler','Williams Camire','Coleman Dunmire','Phyliss Houk'],
    "Weight":[128,180,193,177,237,166,224,208,177,241,114,161,162,151,220,142,193,193,124,130,132,141,190,239,213,131,172,127,184,157,215,122,181,240,218,205,239,217,234,158,180,131,194,171,177,110,117,114,217,123,248,189,198,127,182,121,224,111,151,170,188,150,137,231,222,186,139,175,178,246,150,154,129,216,144,198,228,183,173,129,157,199,186,232,172,157,246,239,214,161,132,208,187,224,164,177,175,224,219,235,112,241,243,179,208,196,131,207,182,233,191,162,173,197,190,182,231,196,196,143,250,174,138,135,164,204,235,192,114,179,215,127,185,213,250,213,153,217,176,190,119,167,118,208,113,206,200,236,159,218,168,159,156,183,121,203,215,209,179,219,174,220,129,188,217,250,166,157,112,236,182,144,189,243,238,147,165,115,160,134,245,174,238,157,150,184,174,134,134,248,199,165,117,119,162,112,170,224,247,217],
    "Membership(Days)":[52,70,148,124,186,157,127,155,37,185,158,129,93,69,124,13,76,153,164,161,48,121,167,69,39,163,7,34,176,169,108,162,195,86,155,77,197,200,80,142,179,67,58,145,188,147,125,15,13,173,125,4,61,29,132,110,62,137,197,135,162,174,32,151,149,65,18,42,63,62,104,200,189,40,38,199,1,12,8,2,195,30,7,72,130,144,2,34,200,143,43,196,22,115,171,54,143,59,14,52,109,115,187,185,26,19,178,18,120,169,45,52,130,69,168,178,96,22,78,152,39,51,118,130,60,156,108,69,103,158,165,142,86,91,117,77,57,169,86,188,97,111,22,83,81,177,163,35,12,164,21,181,171,138,22,107,58,51,38,128,19,193,157,13,104,89,13,10,26,190,179,101,7,159,100,49,120,109,56,199,51,108,47,171,69,162,74,119,148,88,32,159,65,146,140,171,88,18,59,13]
})
training_data.head(10)


# In[8]:


# Collecting a summary of all numeric data
training_df.describe()


# In[9]:


# Finding the names of the trainers
training_df["Name"].head()


# In[10]:


# Finding how many students each trainer has
stu_per_train = training_df["Trainer"].value_counts()
stu_per_train


# In[11]:


# Finding the average weight of all students
average_weight = training_df["Weight"].mean()
average_weight


# In[12]:


# Finding the combined weight of all students
sum_weight = training_df["Weight"].sum()
sum_weight


# In[13]:


# Converting the membership days into weeks and then adding a column to the DataFrame
weeks = training_df["Membership(Days)"]/7
training_df["Membership (Weeks)"] = weeks

training_df.head()
