from source.app import calculate_vwap


def test_vwap_calculation_with_empty_data(capsys):
    data = [{'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141577.59078863}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141577.66285668}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141577.686401}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.53947451}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141577.68991539}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141577.70222182}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.54106861}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.5435541}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.54610861}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141577.7262681}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141578.18551662}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141578.22492647}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141578.26433632}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141578.2837332}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141578.2990432}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141578.30153473}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.55874735}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.5607134}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.5607526}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.5652126}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.5800426}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.5804246}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141578.30602651}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141579.41339745}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141579.46714889}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141579.68537174}, {'product_id': 'ETH-BTC', 'price': 0.07015666666666666, 'volume': 9000.11270412}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141579.69633239}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141580.07493889}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141580.40965766}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141580.45627283}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.58547312}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.58629662}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7670.83413942}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7671.03315434}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7671.12666275}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7671.14065071}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7671.38848388}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7671.42848388}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7671.47053127}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7671.51053127}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.02404053}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.21104373}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141582.71727283}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.21119186}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.21141064}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141583.11727283}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141583.21727283}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141584.19838283}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141586.69738283}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141586.89738283}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141588.04738283}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141588.62122611}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141589.27122611}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141590.12122611}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141593.24155197}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141593.28096182}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141593.38358182}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141593.42298182}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.21553964}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.21716311}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141593.54008649}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.21746811}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141594.14787649}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.21840154}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.2184867}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.21887301}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.22373015}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.2266161}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141594.55231772}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.2267811}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.2275211}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.22752231}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.2347811}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.23552231}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.23556996}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.23637517}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141594.78489772}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141594.78589772}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141594.86207939}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.24446942}, {'product_id': 'ETH-BTC', 'price': 0.07015666666666666, 'volume': 9000.2248673}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141594.90259126}, {'product_id': 'ETH-BTC', 'price': 0.07015666666666666, 'volume': 9000.41606071}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.26065791}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141594.90294426}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.26074156}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.26107177}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141595.18827437}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.26207963}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141595.1906404}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.2661404}, {'product_id': 'ETH-BTC', 'price': 0.07015666666666666, 'volume': 9000.88246703}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141595.2014804}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141595.20242931}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141595.2261247}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.26628977}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.2664378}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.26762714}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.27370714}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.27396071}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.08437573}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.1128384}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.7073647}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.70737248}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.7358247}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.2739632}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.73583515}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.74971368}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.28671021}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.28749891}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.30025035}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.79867823}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.82713823}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.8271409}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141596.8331409}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141597.0051409}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141597.01702965}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141597.19502965}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.3226219}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.35141343}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.36601567}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.61378369}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.70025049}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141597.76798965}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141598.34094965}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141599.21035199}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141600.79856953}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.70893902}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.70901049}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141600.8270322}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141600.85549487}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141600.85726659}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141600.8920583}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141601.062825}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141601.36003729}, {'product_id': 'ETH-BTC', 'price': 0.07015666666666666, 'volume': 9000.90625678}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141601.65724958}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.23020958}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.25867225}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.28713492}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.31559759}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.71651049}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.71739612}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.36234029}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.41234029}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.41338622}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.74167886}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.53166864}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.53252373}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.75604431}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.77040976}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.7710342}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.53752373}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.55879373}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.55879696}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141602.58506373}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.7711172}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.17951373}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.17952274}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.20579597}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.2320692}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.27951373}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.30578373}, {'product_id': 'ETH-BTC', 'price': 0.07015666666666666, 'volume': 9000.93003429}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.77190593}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.33205373}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.33205696}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.63461243}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.74331243}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.76957373}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.77392848}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141603.77153336}, {'product_id': 'ETH-BTC', 'price': 0.07015666666666666, 'volume': 9000.93083904}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141604.36588647}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141604.71583336}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141604.71588647}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141604.75112483}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141605.10086688}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.77398548}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.78829393}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.80265938}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141605.10586688}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141606.20657996}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141606.31021688}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.80359496}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141607.30729304}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141607.70421688}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141608.80992995}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141611.58726561}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141614.38784146}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.81359496}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.81788148}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.832168}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.83222032}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141614.64476315}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.83246374}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141614.6523368}, {'product_id': 'BTC-USD', 'price': 61425.34333333333, 'volume': 7672.83437571}, {'product_id': 'ETH-USD', 'price': 4296.9800000000005, 'volume': 141614.7688906}]
    calculate_vwap(data)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_vwap_calculation_with_200_data(capsys):
    data = {
        "key1": 1
    }
    calculate_vwap(data)
    captured = capsys.readouterr()
    assert captured.out == (
            "BTC-USD Volume Weighted Average Price is 61425.34333333333\n"
            "ETH-USD Volume Weighted Average Price is 4296.98\n"
            "ETH-BTC Volume Weighted Average Price is 0.07015666666666666\n"
        )