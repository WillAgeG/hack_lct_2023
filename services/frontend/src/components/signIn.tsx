/* eslint-disable @next/next/no-img-element */
"use client";

import { switchState } from "@/redux/slices/authSlice";
import axios from "axios";
import { Merriweather } from "next/font/google";
import { useDispatch } from "react-redux";

const font = Merriweather({ subsets: ['latin', 'cyrillic'], weight: "700" })

export default function SignInForm() {

    const dispatch = useDispatch();

    const hide = (e: React.MouseEvent) => {
        const item = e.target as HTMLElement
        if (item.classList.contains("popup")) { dispatch(switchState()) };
    }

    const signIn = (e: React.FormEvent) => {
        e.preventDefault();
        const form = e.target as HTMLElement
        const data: any = {}

        form.querySelectorAll("input").forEach((item: HTMLInputElement) => {
            data[item.id] = item.value;
        })

        axios.post("/token/login", data).then((res) => {
            console.log(res.data)
        })
    }

    const signInGoogle = async () => {
        const authURL = await axios.get(`accounts/auth/o/google-oauth2?redirect_uri=https`).then((res) => { return res.data })
        window.location.href = authURL.authorization_url

    }

    return (
        <div
            className="
                popup fixed top-0 left-0 h-[100vh] w-[100vw] 
                bg-[#00000080] backdrop-blur-sm z-[1]
            "
            onClick={hide}
        >
            <div className="
                rounded-[24px] w-[60%] h-[60%] bg-white absolute flex
                top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%]
                items-center justify-between px-[2.5%] 
            " >
                <img
                    src="/images/left-2x.png" alt=""
                    className="w-[56%]"
                />
                <div className="flex flex-col items-center justify-center w-[40%]">
                    <img src="/icons/clearLogo.png" alt="" />
                    <h2 className={`text-4xl mt-[16px] ${font.className}`}>Вход в компас</h2>
                    <form className="flex flex-col w-[100%] mt-[16px]" onSubmit={signIn}>
                        <input
                            id="login" type="text" placeholder="Введите логин" required
                            className="w-[100%] mt-[16px] border-2 rounded-[8px] px-[12px] py-[8px]"
                        />
                        <input
                            id="password" type="text" placeholder="Введите пароль" required
                            className="w-[100%] mt-[16px] border-2 rounded-[8px] px-[12px] py-[8px]"
                        />
                        <div className="flex items-center justify-between mt-[16px] w-[100%]">
                            <div className="w-[40%] h-[1px] bg-black" /><p>или</p><div className="w-[40%] h-[1px] bg-black" />
                        </div>
                        <div className="w-[100%] flex items-center justify-center">
                            <div className="w-auto flex rounded-[12px] border-[1px] px-[12px] items-center justify-center mt-[16px] py-[4px] cursor-pointer hover:bg-slate-200 border-black" onClick={signInGoogle}>
                                <img className="w-[24px]" src="/icons/google.png" alt="" />
                                <p className="ml-[8px]">Sign in with google</p>
                            </div>
                        </div>
                        <button className="btn bg-db px-[32px] py-[12px] rounded-[8px] mt-[16px]">Продолжить</button>
                    </form>
                </div>

            </div>
        </div>
    )
}
