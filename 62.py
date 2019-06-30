marketing = ['loyality program', 'client promotion', 'market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2, 'investor relations')
print(marketing)
#emailMarketing = marketing.copy() - również działa, rozwiązanie z Udemy
emailMarketing = list(marketing)
print(emailMarketing)
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal communication']
print(internalEmails)
#emailMarketing.extend(internalEmails) - również działa, rozwiązanie z Udemy - i nie ma kwadratowego nawiasa
emailMarketing.append(internalEmails)
print(emailMarketing)
tuple = tuple(emailMarketing)
print(tuple)