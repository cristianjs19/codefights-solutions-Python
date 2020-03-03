def findEmailDomain(address):
        for i in range(len(address)):
                if address[i] == "@":
                        dom = address[i+1:]

        return dom