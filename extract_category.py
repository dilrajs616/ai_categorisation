file_path = "categories.txt"  # Change this to your actual file path

# Initialize an empty list to store the extracted data
available_categories = ['Beauty', 'Education', 'Business', 'Environment', 'Cloudflare', 'Blogs And Forums', 'Hobbies And Interests', 'Tourism', 'Security And Defense', 'Food And Beverages', 'News', 'Research', 'Drugs', 'Adult And Dating', 'Finance', 'Tourism', 'Business', 'Life', 'Unknown', 'Automobiles And Transportation', 'Non Governmental Organization', 'Home And Garden', 'Alcohol And Tobacco', 'Fashion', 'Social Media Networking', 'Hacking', 'Pornography', 'Restaurants And Dining', 'Gaming', 'Gambling', 'Advertisements', 'Politics', 'Entertainment', 'Pets And Animals', 'Agriculture', 'Healthcare', 'Health', 'Society And Culture', 'Real Estate And Property', 'Construction', 'Search Engines', 'Articles', 'Medicine', 'Government', 'Parked Domain', 'Religious', 'Biography', 'Education', 'Sports', 'Personal And Portfolio Website', 'Technology', 'Logistics', 'Intolerance And Hate', 'Services and Repair', 'Stock Market', 'Ecommerce And Shopping', 'Astrology', 'Jobs Search']

# new_categories = []

# with open(file_path, "r") as file:
#     for line in file:
#         category = line.strip()
#         if category and category not in available_categories:
#             new_categories.append(category)

# Remove duplicates and sort
unique_list = sorted(set(available_categories))

# Print the sorted list of new categories
print(unique_list)