counties = ["Arapahoe","Denver","Jefferson"]
#print(counties)
#print(counties[0])
#print(counties[2])
##-to know the second to last item in list, -1 to know the last item
#print(counties[-2])
#print(len(counties))
##slicing to get the first 2 items in counties
#print(counties[0 : 2])
##slice to get the first item in counties
#print(counties[0 : 1])
##slice to get the first and second  and third items from the counties
#print(counties[ : 3])
##slice to get items after the first item
#print(counties[1:])
#counties.append("El Paso")
#print(counties)
#counties.insert(2, "El Paso")
#print(counties)
#counties.remove("El Paso")
#print(counties)
#counties.insert(3, "El Paso")
#print(counties)
#print(counties.pop(-1))
#print(counties)
#
#counties.insert(3, "El Paso")
#print(counties)
#print(counties.pop(3))
#print(counties)
#print(counties)
##Add El Paso to the second position in the list. 
counties.insert(1, "El Paso")
#print(counties)
##Remove Arapahoe from the list.
counties.remove("Arapahoe")
print(counties)
##Make Denver the third item in the list, but keep Jefferson the second item in the list.
counties[1] = "Jefferson"
counties[2] = "Denver"
print(counties)
##Add Arapahoe to the list. 
counties.append("Arapahoe")
print(counties)
