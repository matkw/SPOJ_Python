# GLUTTON
T = int(input())
daytime_ = int(86400)
cookies_required = int(0)
for i in range(T):
    amount_of_gluttons, amount_of_cookies_in_pack = map(int, input().split())
    for x in range(amount_of_gluttons):
        glutton_eating_time = int(input())
        cookies_required += int(daytime_ / glutton_eating_time) #+ (daytime_ % glutton_eating_time > 0)
    pack_of_cookies_required = int(cookies_required / amount_of_cookies_in_pack) + (
                cookies_required % amount_of_cookies_in_pack > 0)
    print(pack_of_cookies_required)
    cookies_required = int(0)
