/* eslint-disable @next/next/no-img-element */
"use client";
import { switchState } from '@/redux/slices/authSlice'
import { Merriweather } from 'next/font/google'
import { useDispatch } from 'react-redux';
import { useRouter } from 'next/router';
import Link from 'next/link'
import { useEffect } from 'react';
import axios from 'axios';

const font = Merriweather({ subsets: ['latin', 'cyrillic'], weight: "700" })

export default function Home() {

	const dispatch = useDispatch();
	const router = useRouter();

	const { code, state } = router.query;

	useEffect(() => {
		if (!code || !state) return
		axios.post("accounts/auth/o/google-oauth2/", { code, state })
			.then((res) => {
				console.log(res.data)
			})

	}, [code, state])

	return (
		<>
			<img src="/images/left.png" alt="" className='w-[20%]' />
			<div className='flex flex-col justify-between w-[56%]'>
				<h1 className={`
				 	text-[5em] text-center font-[900] 
					leading-[91px] ${font.className} text-[#0A2351]
				`}>Компас — твой свет в мире профессий</h1>
				<div className="flex justify-around mt-[60px] w-[100%]">
					<Link href="/auth" className="btn large-btn w-[40%] py-[16px]">Регистрация</Link>
					<button
						className="btn large-btn w-[40%] py-[16px] bg-db"
						onClick={() => { dispatch(switchState()) }}
					>Авторизация</button>
				</div>
				<div className='flex justify-around mt-[80px]'>
					<img src="/icons/prof.svg" alt="" />
					<img src="/icons/analyze.svg" alt="" />
					<img src="/icons/sovet.svg" alt="" />
				</div>
			</div>
			<img src="./images/right.png" alt="" className='w-[20%]' />
		</>
	)
}
