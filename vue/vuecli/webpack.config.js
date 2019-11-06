// webpack의 기본적인 설정
// BASE_DIR같은 기본 경로
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')
module.exports = {
    mode: 'development',
    // 여러개의 파일을 읽어오는 작업.
    entry: {
        // 읽어오는 작업. src/main.js에서 읽어올거야
        app: path.join(__dirname, 'src', 'main.js')
    },
    // 관련된 모듈
    module: {
        rules: [
            {
                test: /\.vue$/,    // 정규표현식. vue라는 확장자를 가진 애들은
                use: 'vue-loader', // 모두 vue-loader로 번역을 해라!
            },
            {
                test: '/\.css$/',
                use: ['vue-style-loader', 'css-loader'] // 앞에꺼가 css를 만들거고 뒤에꺼가 그거를 불러와서 처리해줄거다...?
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin()
    ],
    // 최종 결과
    output: {
        filename: 'app.js', // 이런 이름으로 결과를 내보내줘!
        // 최종 결과의 경로
        path: path.join(__dirname, 'dist')
    }
}