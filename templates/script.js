const ZaimApp = {
    initData: Telegram.WebApp.initData || '',
    initDataUnsafe: Telegram.WebApp.initDataUnsafe || {},
    MainButton: Telegram.WebApp.MainButton,

    init(options) {
        document.body.style.visibility = '';
        Telegram.WebApp.ready();
        Telegram.WebApp.MainButton.setParams({
            text: 'Закрыть сайт',
            is_visible: true
        }).onClick(DemoApp.close);
    },
    close() {
        Telegram.WebApp.close();
    },
};