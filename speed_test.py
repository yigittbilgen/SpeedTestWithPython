import speedtest

def speed_test():
    st = speedtest.Speedtest()
    servers = st.get_best_server()
    print("Download Test Starting...")
    download_test = st.download() / 1000000
    print("Upload Test Starting...")
    upload_test = st.upload() / 1000000

    return download_test, upload_test

if __name__ == "__main__":
    download_test, upload_test = speed_test()
    print("Download Speed: {:.2f} Mbps".format(download_test))
    print("Upload Speed: {:.2f} Mbps".format(upload_test))