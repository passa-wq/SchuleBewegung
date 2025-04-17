from time import sleep

async def testAsync():
    print("Start")
    sleep(5)
    print("End")

testAsync()
print("Währendessen")