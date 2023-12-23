/* eslint-disable @next/next/no-img-element */
"use client";
import InputField from '@/components/inputField'
import axios from 'axios'
import { Merriweather } from 'next/font/google'

const font = Merriweather({ subsets: ['latin', 'cyrillic'], weight: "700" })

const inputs = [
    {
        id: "name", type: "text",
        label: "Имя", placeholder: "Введите имя"
    },
    {
        id: "surname", type: "text",
        label: "Фамилия", placeholder: "Введите фамилию"
    },
    {
        id: "sex", type: "text",
        label: "Пол", placeholder: "Мужской"
    },
    {
        id: "birthDate", type: "date",
        label: "Дата рождения", placeholder: "-"
    },
    {
        id: "youtube", type: "text",
        label: "Ссылка на Youtube", placeholder: "Введите ссылку на Youtube"
    },
    {
        id: "vk", type: "text",
        label: "Ссылка на VK", placeholder: "Введите ссылку на VK"
    },
    {
        id: "login", type: "text",
        label: "Логин", placeholder: "Введите логин"
    },
    {
        id: "password", type: "password",
        label: "Пароль", placeholder: "Введите пароль"
    }
]

export default function Home() {
    const signUp = (e: React.FormEvent) => {
        e.preventDefault();
        const form = e.target as HTMLElement
        const data: any = {}

        form.querySelectorAll("input").forEach((item: HTMLInputElement) => {
            data[item.id] = item.value;
        })
        console.log(data);
        axios.post("/token/login", data).then((res) => {
            console.log(res.data)
        })
    }

    return (
        <>
            <img src="/images/left-2x.png" alt="" className='w-[46%]' />
            <div className={`flex flex-col justify-between items-start w-[50%]`}>
                <h2 className={`text-5xl ${font.className}`}>Найди свое будущее здесь и сейчас - вместе с Компас</h2>
                <div>
                    <h3 className={`text-2xl mt-[20px] ${font.className}`}>Форма регистрации</h3>
                    <form action="" className="flex flex-wrap justify-between mt-[12px]" onSubmit={signUp}>
                        {inputs.map((item, i) => {
                            return (
                                <InputField
                                    key={item.id + i} type={item.type}
                                    placeholder={item.placeholder} label={item.label}
                                    className="w-[45%] mt-[12px]"
                                />
                            )
                        })}
                        <div className="flex w-[100%] mt-[16px] items-center">
                            <input
                                id="confirm" type="checkbox" required
                                className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                            />
                            <label htmlFor="confirm" className="ml-[8px]">Я принимаю условия пользовательского соглашения</label>
                        </div>
                        <button className="btn w-[30%] py-[16px] mt-[20px] bg-db">Далее</button>
                    </form>
                </div>
            </div>
        </>
    )
}
